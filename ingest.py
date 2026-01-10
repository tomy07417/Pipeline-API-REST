import requests
import time
import pandas as pd

def fetch_data(url, params: dict = None, logger=None, max_retries: int = 3, backoff_factor: float = 2.0):

    logger.info(f"Fetching {params.get('rows')} rows of {params.get('type')} data...")
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params)
            return response.json()
        except requests.RequestException as e:
            if attempt == max_retries - 1:
                logger.error(f"All {max_retries} attempts failed. Error: {e}")
                response.raise_for_status()

            wait_time = backoff_factor ** attempt
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

def parse_data(data: dict):
    tables_name = data.get('tables', {}).keys()
    tables = {}

    for table in tables_name:
        table_data = data['tables'][table]
        tables[table] = pd.json_normalize(table_data)
        tables[table] = pd.DataFrame(tables[table])

    return tables

    