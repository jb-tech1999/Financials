import pandas as pd
import datetime

def clean_data(df):
    # Replace gaps forward from the previous valid value in: 'Category'
    df = df.fillna({'Category': df['Category'].ffill()})
    # Filter rows based on column: 'Category'
    df = df[df['Category'] != "Total spend"]
    #drop rows where Sub-Category is null
    df = df.dropna(subset=['Sub-Category'])
    return df

def extract_year(df):
    # Convert column: 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    # Extract year from column: 'Date'
    df['Year'] = df['Date'].dt.year
    return df


def melt_data(df):
    # Melt the dataframe
    df_melted = pd.melt(df, id_vars=['Category','Sub-Category'], var_name='Date', value_name='Amount')
    return df_melted

def fix_dates(df):
    df_columns_list = df.columns.tolist()
    #get months from df
    months_list = df_columns_list[2:]
    # Get the current year
    current_year = datetime.datetime.now().year
    # Initialize an empty list to store the generated dates
    date_list = ['Category','Sub-Category']
    # Initialize a variable to keep track of the year
    year = current_year

    # Iterate through the month strings
    for month_str in months_list:
        # Extract the month and year information
        parts = month_str.split()
        month = parts[0]
        if month.count(".") == 1:
            # strip dot and all after it
            month = month.split(".")[0]

        # If a year is present in the month string, update the year
        if len(parts) > 1:
            year = int(parts[1])

        # Create a date string in the format "Month Year"
        date_str = f"01-{month}-{year}"

        # Append the date string to the list
        date_list.append(date_str)

    #update column names
    df.columns = date_list
    return df
