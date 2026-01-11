import pandas as pd
import os

def transform_categories(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the categories DataFrame by handling missing values and converting data types.

    Parameters:
    df (pd.DataFrame): The input categories DataFrame.

    Returns:
    pd.DataFrame: The transformed categories DataFrame.
    """
    df['category_name'] = df['category_name'].fillna('Unknown').astype('category')
    df['parent_category_id'] = df['parent_category_id'].astype('Int64')

    return df

def transform_brands(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform brand names in a DataFrame by handling missing values and optimizing data type.

    Args:
        df (pd.DataFrame): Input DataFrame
    Returns:
        pd.DataFrame: The transformed brands Dataframe
    """

    df['brand_name'] = df['brand_name'].fillna('Unknown').astype('category')

    return df

def transform_suppliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform suppliers DataFrame by optimizing data types and handling missing values.

    Args:
        df (pd.DataFrame): Input suppliers DataFrame
    Returns:
        pd.DataFrame: The transformed suppliers DataFrame
    """
    df['supplier_name'] = df['supplier_name'].fillna('Unknown')
    df['contact_name'] = df['contact_name'].fillna('Unknown')
    df['email'] = df['email'].fillna('-').str.lower()
    df['phone'] = df['phone'].fillna('-')
    df['address'] = df['address'].fillna('-')
    df['rating'] = df['rating'].fillna(0.0).astype('float32')
    df['is_active'] = df['is_active'].astype(bool)

    return df

def transform_warehouses(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform warehouses DataFrame by optimizing data types.

    Args:
        df (pd.DataFrame): Input warehouses DataFrame
    Returns:
        pd.DataFrame: The transformed warehouses DataFrame
    """
    df['warehouse_name'] = df['warehouse_name'].fillna('Unknown')
    df['location'] = df['location'].fillna('Unknown')
    df['capacity_units'] = df['capacity_units'].astype('int32')
    df['current_occupancy'] = df['current_occupancy'].astype('int32')
    df['manager_name'] = df['manager_name'].fillna('Unknown')

    return df

def transform_products(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform products DataFrame by converting dates and optimizing data types.

    Args:
        df (pd.DataFrame): Input products DataFrame
    Returns:
        pd.DataFrame: The transformed products DataFrame
    """
    df['sku'] = df['sku'].fillna('-').astype(str)
    df['product_name'] = df['product_name'].fillna('Unknown')
    df['description'] = df['description'].fillna('-')
    df['category_id'] = df['category_id'].dropna().astype('int64')
    df['brand_id'] = df['brand_id'].dropna().astype('int64')
    df['supplier_id'] = df['supplier_id'].dropna().astype('int64')
    df['price'] = df['price'].fillna(0.0).astype('float32')
    df['cost'] = df['cost'].fillna(0.0).astype('float32')
    df['weight_kg'] = df['weight_kg'].fillna(0.0).astype('float32')
    df['is_active'] = df['is_active'].astype(bool)
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    df['updated_at'] = pd.to_datetime(df['updated_at'], errors='coerce')

    return df

def transform_inventory(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform inventory DataFrame by converting dates and optimizing data types.

    Args:
        df (pd.DataFrame): Input inventory DataFrame
    Returns:
        pd.DataFrame: The transformed inventory DataFrame
    """
    df['product_id'] = df['product_id'].astype('int64')
    df['warehouse_id'] = df['warehouse_id'].astype('int64')
    df['quantity'] = df['quantity'].fillna(0).astype('int32')
    df['min_stock_level'] = df['min_stock_level'].fillna(0).astype('int32')
    df['max_stock_level'] = df['max_stock_level'].fillna(0).astype('int32')
    df['last_restock_date'] = pd.to_datetime(df['last_restock_date'], errors='coerce')

    return df

def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform customers DataFrame by converting dates, handling PII and optimizing data types.

    Args:
        df (pd.DataFrame): Input customers DataFrame
    Returns:
        pd.DataFrame: The transformed customers DataFrame
    """
    df['first_name'] = df['first_name'].fillna('Unknown')
    df['last_name'] = df['last_name'].fillna('Unknown')
    df['email'] = df['email'].fillna('-').str.lower()
    df['phone'] = df['phone'].fillna('-')
    df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')
    df['city'] = df['city'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    df['postal_code'] = df['postal_code'].astype('int64')
    df['segment'] = df['segment'].fillna('Unknown').astype('category')
    df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce')
    df['last_login'] = pd.to_datetime(df['last_login'], errors='coerce')
    df['is_verified'] = df['is_verified'].astype(bool)
    df['accepts_marketing'] = df['accepts_marketing'].astype(bool)

    return df

def transform_promotions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform promotions DataFrame by converting dates and optimizing data types.

    Args:
        df (pd.DataFrame): Input promotions DataFrame
    Returns:
        pd.DataFrame: The transformed promotions DataFrame
    """
    df['promotion_code'] = df['promotion_code'].dropna().astype(str)
    df['promotion_name'] = df['promotion_name'].fillna('Unknown')
    df['promotion_type'] = df['promotion_type'].fillna('Unknown').astype('category')
    df['discount_value'] = df['discount_value'].fillna(0).astype('int32')
    df['min_order_amount'] = df['min_order_amount'].fillna(0).astype('int32')
    df['max_uses'] = df['max_uses'].fillna(0).astype('int32')
    df['current_uses'] = df['current_uses'].fillna(0).astype('int32')
    df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce')
    df['end_date'] = pd.to_datetime(df['end_date'], errors='coerce')
    df['is_active'] = df['is_active'].astype(bool)

    return df

def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform orders DataFrame by converting dates, handling nulls and optimizing data types.

    Args:
        df (pd.DataFrame): Input orders DataFrame
    Returns:
        pd.DataFrame: The transformed orders DataFrame
    """
    df['order_number'] = df['order_number'].fillna('Unknown').astype(str)
    df['customer_id'] = df['customer_id'].astype('int64')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['status'] = df['status'].fillna('Unknown').astype('category')
    df['subtotal'] = df['subtotal'].fillna(0.0).astype('float32')
    df['discount_percent'] = df['discount_percent'].fillna(0).astype('int32')
    df['shipping_cost'] = df['shipping_cost'].fillna(0).astype('int32')
    df['tax_amount'] = df['tax_amount'].fillna(0.0).astype('float32')
    df['total_amount'] = df['total_amount'].fillna(0.0).astype('float32')
    df['payment_method'] = df['payment_method'].fillna('Unknown').astype('category')
    df['shipping_method'] = df['shipping_method'].fillna('Unknown').astype('category')
    df['promotion_id'] = df['promotion_id'].astype('Int64')
    df['notes'] = df['notes'].fillna('-')

    return df

def transform_order_items(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform order_items DataFrame by optimizing data types.

    Args:
        df (pd.DataFrame): Input order_items DataFrame
    Returns:
        pd.DataFrame: The transformed order_items DataFrame
    """
    df['order_id'] = df['order_id'].astype('Int64')
    df['product_id'] = df['product_id'].astype('Int64')
    df['quantity'] = df['quantity'].fillna(0).astype('int32')
    df['unit_price'] = df['unit_price'].fillna(0.0).astype('float32')
    df['subtotal'] = df['subtotal'].fillna(0.0).astype('float32')

    return df

def transform_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform reviews DataFrame by converting dates and optimizing data types.

    Args:
        df (pd.DataFrame): Input reviews DataFrame
    Returns:
        pd.DataFrame: The transformed reviews DataFrame
    """
    df['product_id'] = df['product_id'].astype('Int64')
    df['customer_id'] = df['customer_id'].astype('Int64')
    df['rating'] = df['rating'].fillna(0).astype('float16')
    df['title'] = df['title'].fillna('-')
    df['comment'] = df['comment'].fillna('-')
    df['is_verified_purchase'] = df['is_verified_purchase'].astype(bool)
    df['helpful_votes'] = df['helpful_votes'].fillna(0).astype('int32')
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')

    return df

TRANSFORMERS = {
    'categories': transform_categories,
    'brands': transform_brands,
    'suppliers': transform_suppliers,
    'warehouses': transform_warehouses,
    'products': transform_products,
    'inventory': transform_inventory,
    'customers': transform_customers,
    'promotions': transform_promotions,
    'orders': transform_orders,
    'order_items': transform_order_items,
    'reviews': transform_reviews
}

def save_dataframe(df: pd.DataFrame, table_name: str, output_dir: str) -> None:
    """
    Save the DataFrame to a CSV file in the specified output directory.

    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    table_name (str): The name of the table (used for the filename).
    output_dir (str): The directory where the CSV file will be saved.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_path = os.path.join(output_dir, f"{table_name}.parquet")
    df.to_parquet(file_path, index=False, engine="pyarrow")

def save_orders(orders: pd.DataFrame, order_items: pd.DataFrame, output_dir: str) -> None:
    """
    Save orders and order_items DataFrames to CSV files in the specified output directory.

    Parameters:
    orders (pd.DataFrame): The orders DataFrame to save.
    order_items (pd.DataFrame): The order_items DataFrame to save.
    output_dir (str): The directory where the CSV files will be saved.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    min_year = orders['order_date'].dt.year.min()
    max_year = orders['order_date'].dt.year.max()

    for year in range(min_year, max_year + 1):
        for m in range(1, 13):
            if not os.path.exists(os.path.join(output_dir, str(year))):
                os.makedirs(os.path.join(output_dir, str(year)))

            if not os.path.exists(os.path.join(output_dir, str(year), str(m))):
                os.makedirs(os.path.join(output_dir, str(year), str(m)))

            monthly_orders = orders[(orders['order_date'].dt.year == year) & (orders['order_date'].dt.month == m)]
            monthly_order_items = order_items[order_items['order_id'].isin(monthly_orders['order_id'])]

            monthly_order_items.to_parquet(
                os.path.join(output_dir, str(year), str(m), "order_items.parquet"))

            monthly_orders.to_parquet(
                os.path.join(output_dir, str(year), str(m), "orders.parquet"))