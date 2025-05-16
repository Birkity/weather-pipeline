
# Weather Data Processing Pipeline

This repository contains a data pipeline to ingest, clean, transform, and analyze weather data using Python. The pipeline is modular, retains all data for maximum insights, and includes multiple visualizations to explore weather patterns across cities.

## Project Structure

- `data/`: Contains the input CSV file (`weather_data.csv`).
- `outputs/`: Contains the transformed data, temperature report, and visualizations.
- `notebooks/`: Contains the Jupyter Notebook (`weather_pipeline.ipynb`) to run the pipeline.
- `src/`: Contains modular Python scripts for each pipeline step.
- `requirements.txt`: Lists the required Python packages.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Birkity/weather-pipeline.git
   cd weather_pipeline
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/weather_pipeline.ipynb
   ```
   Execute the cells in the notebook to run the pipeline and generate outputs.

## Approach

- **Modularity**: The pipeline is split into separate modules (`data_ingestion.py`, `data_cleaning.py`, etc.) for better maintainability.
- **Cleaning**: Missing `temperature_celsius` and `humidity_percent` values are filled with city-wise averages, dates are standardized to datetime objects, and all rows are retained (including those with "Unknown" weather conditions).
- **Transformation**: Added a `temperature_fahrenheit` column using the formula:  
  `F = C * 9/5 + 32`.
- **Output**: The transformed data is saved as a CSV, and a Markdown report lists the top 5 cities by average temperature.
- **Visualizations**:
  - Bar chart of average temperatures per city.
  - Line plot of temperature trends over time.
  - Scatter plot of humidity vs wind speed, colored by city and sized by temperature.
  - Pie chart of weather condition distribution.
- **Insights**: A detailed analysis of the visualizations is included in the notebook, covering temperature patterns, weather conditions, humidity and wind speed relationships, and data quality issues.

## Sample Output

- Transformed data: `outputs/transformed_weather_data.csv`
- Temperature report: `outputs/temperature_report.md`
- Visualizations:
  - `outputs/avg_temperature_chart.png`
  - `outputs/temperature_trend.png`
  - `outputs/humidity_vs_wind_speed.png`
  - `outputs/weather_condition_distribution.png`
