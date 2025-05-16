import pandas as pd

def clean_weather_data(df):
    """
    Clean the weather DataFrame by handling missing values and standardizing dates.
    
    Args:
        df (pd.DataFrame): Raw weather data.
    
    Returns:
        pd.DataFrame: Cleaned weather data.
    """
    # Standardize date format to YYYY-MM-DD
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')
    
    # Handle missing temperature by filling with city-wise average
    df['temperature_celsius'] = df.groupby('city')['temperature_celsius'].transform(
        lambda x: x.fillna(x.mean())
    )
    
    # Fill missing weather_condition with "Unknown"
    df['weather_condition'] = df['weather_condition'].fillna('Unknown')
    
    print("Data cleaning completed.")
    return df