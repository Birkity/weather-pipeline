import pandas as pd

def clean_weather_data(df):
    """
    Clean the weather DataFrame by handling missing values and standardizing dates.
    Retains all rows, even with missing or "Unknown" weather conditions.
    
    Args:
        df (pd.DataFrame): Raw weather data.
    
    Returns:
        pd.DataFrame: Cleaned weather data.
    """
    # Standardize date format to datetime object
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # Handle missing temperature by filling with city-wise average
    df['temperature_celsius'] = df.groupby('city')['temperature_celsius'].transform(
        lambda x: x.fillna(x.mean())
    )
    
    # Handle missing humidity by filling with city-wise average
    df['humidity_percent'] = df.groupby('city')['humidity_percent'].transform(
        lambda x: x.fillna(x.mean())
    )
    
    # Fill missing weather_condition with "Unknown"
    df['weather_condition'] = df['weather_condition'].fillna('Unknown')
    
    print("Data cleaning completed.")
    return df