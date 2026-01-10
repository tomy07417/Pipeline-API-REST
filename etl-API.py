import logging
from config import API_TOKEN, EMAIL, API_BASE_URL
from ingest import fetch_data, parse_data
from transform import TRANSFORMERS, save_dataframe

PARAMS = {
    "email": EMAIL,
    "key": API_TOKEN,
    "type": "ecommerce",
    "rows": 1000,
    "format": "json"
}

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)

    try:
        resp = fetch_data(API_BASE_URL, PARAMS, logger)
        tables = parse_data(resp)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return

    for tn, df in tables.items():
        logger.info(f"Table: {tn}")
        logger.info(f"Number of records: {len(df)}")
        logger.info(f"Columns and data types:\n{df.dtypes}")

        logger.info("Transforming data...")
        if tn in TRANSFORMERS:
            transformer = TRANSFORMERS[tn]
            tables[tn] = transformer(df)
        else:
            logger.warning(f"No transformer defined for table: {tn}")
        
        save_dataframe(tables[tn], tn, output_dir='output')

if __name__ == "__main__":
    main()