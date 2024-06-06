"""
Ultility functions for data ingestion and data formatting
"""
import pandas as pd

def format_bigquerydata(data: pd.DataFrame)-> pd.DataFrame:
    """
    clean and format the data from bigquery
    """
    # rule 1: remove columns with all missing values


    # rename columns names
    data.columns = [col.lower().replace(' ', '_') for col in data.columns]
    return data
