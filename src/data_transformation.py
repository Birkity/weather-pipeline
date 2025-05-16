def transform_weather_data(df):
    """
    Transform the weather DataFrame by adding a temperature_fahrenheit column.
    
    Args:
        df (pd.DataFrame): Cleaned weather data.
    
    Returns:
        pd.DataFrame: Transformed weather data.
    """
    # Convert Celsius to Fahrenheit: F = C * 9/5 + 32
    df['temperature_fahrenheit'] = df['temperature_celsius'] * 9/5 + 32
    print("Data transformation completed.")
    return df