""" Main table
join from 2 tables


each country has its own table and they merge to form the main table
they both have a date column

website_visitors_us - date (time, day, month, year)
website_visitors_uk - date (year, month, day, time)


transform date column
convert the data to look the same


one function to convert - use decorator
write a decorator function that implements this """
import pandas as pd
from functools import wraps
import os
import json

def date_format_decorator(combine_fields=None, dayfirst=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            df = func(*args, **kwargs)
            if combine_fields:
                # Combine specified fields into one datetime string
                df['date'] = df[combine_fields[0]].astype(str) + ' ' + df[combine_fields[1]].astype(str)
            elif 'date' not in df.columns:
                raise KeyError("No 'date' column found for date parsing.")
            # Parse combined date string to datetime, flexible format
            df['date'] = pd.to_datetime(df['date'], dayfirst=dayfirst, infer_datetime_format=True, errors='coerce')
            if df['date'].isnull().any():
                print("Warning: Some dates could not be parsed and are set to NaT")
            return df
        return wrapper
    return decorator

@date_format_decorator(combine_fields=['date', 'time'], dayfirst=True)  # For US: "date" dd/mm/yyyy + "time" e.g. 2:00 PM
def load_us_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)

@date_format_decorator(combine_fields=['date', 'time'], dayfirst=False)  # For UK: "date" yyyy-mm-dd + "time"
def load_uk_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def etl():
    us_path = os.path.join(os.path.dirname(__file__), 'website_visitors_us.json')
    uk_path = os.path.join(os.path.dirname(__file__), 'website_visitors_uk.json')
    df_us = load_us_data(us_path)
    df_uk = load_uk_data(uk_path)
    main_table = pd.concat([df_us, df_uk], ignore_index=True, sort=False)
    return main_table

if __name__ == "__main__":
    main_df = etl()
    print(main_df)
