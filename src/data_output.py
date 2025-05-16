import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def save_transformed_data(df, output_path):
    """
    Save the transformed DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): Transformed weather data.
        output_path (str): Path to save the CSV file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Transformed data saved to {output_path}")

def generate_temperature_report(df, report_path):
    """
    Generate a Markdown report with the top 5 cities by average temperature.
    
    Args:
        df (pd.DataFrame): Transformed weather data.
        report_path (str): Path to save the report.
    """
    top_cities = df.groupby('city')['temperature_celsius'].mean().nlargest(5).round(2)
    with open(report_path, 'w') as f:
        f.write("# Top 5 Cities by Average Temperature (Celsius)\n\n")
        for city, temp in top_cities.items():
            f.write(f"- {city}: {temp}°C\n")
    print(f"Temperature report saved to {report_path}")

def plot_visualizations(df, output_dir):
    """
    Generate and save multiple visualizations for weather data insights.
    
    Args:
        df (pd.DataFrame): Transformed weather data.
        output_dir (str): Directory to save the plots.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Visualization 1: Average Temperature per City (Bar Chart)
    avg_temp = df.groupby('city')['temperature_celsius'].mean().sort_values()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='temperature_celsius', y=avg_temp.index, hue=avg_temp.index, 
                data=avg_temp.to_frame(), palette='coolwarm', legend=False)
    plt.title('Average Temperature per City (Celsius)', fontsize=14)
    plt.xlabel('Temperature (°C)', fontsize=12)
    plt.ylabel('City', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'avg_temperature_chart.png'))
    plt.close()
    
    # Visualization 2: Temperature Trend Over Time (Line Plot)
    plt.figure(figsize=(12, 6))
    for city in df['city'].unique():
        city_data = df[df['city'] == city].sort_values('date')
        plt.plot(city_data['date'], city_data['temperature_celsius'], marker='o', label=city)
    plt.title('Temperature Trend Over Time', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'temperature_trend.png'))
    plt.close()
    
    # Visualization 3: Humidity vs Wind Speed (Scatter Plot)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='humidity_percent', y='wind_speed_kph', hue='city', size='temperature_celsius', 
                    palette='viridis', sizes=(20, 200))
    plt.title('Humidity vs Wind Speed by City', fontsize=14)
    plt.xlabel('Humidity (%)', fontsize=12)
    plt.ylabel('Wind Speed (kph)', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'humidity_vs_wind_speed.png'))
    plt.close()
    
    # Visualization 4: Weather Condition Distribution (Pie Chart)
    weather_counts = df['weather_condition'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    plt.title('Weather Condition Distribution', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'weather_condition_distribution.png'))
    plt.close()
    
    print("Visualizations saved to outputs/")