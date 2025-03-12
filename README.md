# Airplane Crash Database and Analysis

This project aims to create a comprehensive database of airplane crashes and perform statistical analysis and predictive modeling to understand the factors contributing to these incidents.

## Table of Contents
- [Introduction](#introduction)
- [Data Sources](#data-sources)
- [Database Schema](#database-schema)
- [Data Extraction](#data-extraction)
- [Data Analysis and Modeling](#data-analysis-and-modeling)
- [Results](#results)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Air travel remains one of the safest modes of transportation, but incidents and accidents still occur. This project aims to create a detailed database of airplane crashes, analyze the data to identify patterns and trends, and develop predictive models to help understand the factors that contribute to these accidents.

## Data Sources
The primary sources of data for this project are:
- [National Transportation Safety Board (NTSB)](https://www.ntsb.gov/Pages/AviationQueryv2.aspx)
- [Aviation Safety Network (ASN)](https://asn.flightsafety.org/)

## Database Schema
The database schema is designed to store detailed information about airplane crashes. The main table is `airplane_crashes`, which includes the following fields:
- `id`: Unique identifier for each crash
- `event_date`: Date of the crash
- `location`: Location of the crash
- `operator`: Operator of the aircraft
- `aircraft_type`: Type of the aircraft
- `registration`: Registration number of the aircraft
- `flight_number`: Flight number
- `route`: Route of the flight
- `fatalities`: Number of fatalities
- `description`: Description of the crash
- `source_url`: URL of the source of the information

## Data Extraction
Data is extracted from the NTSB and ASN websites using web scraping techniques and stored in the `airplane_crashes` table. The extraction script is written in Python and uses the `requests` and `beautifulsoup4` libraries.

## Data Analysis and Modeling
The analysis and modeling section includes:
- **Exploratory Data Analysis (EDA)**: Visualizing and understanding the data.
- **Statistical Analysis**: Identifying patterns and trends.
- **Predictive Modeling**: Building and evaluating models to predict airplane crashes.

### Exploratory Data Analysis (EDA)
EDA involves visualizing the distribution of crashes over time, geographical locations, operators, aircraft types, and other factors.

### Statistical Analysis
Statistical tests and models are used to identify significant factors contributing to airplane crashes.

### Predictive Modeling
Machine learning models are developed to predict the likelihood of airplane crashes based on various factors. The models are evaluated using metrics such as accuracy, precision, recall, and F1-score.

## Results
The results section presents the findings from the data analysis and modeling, including visualizations, statistical summaries, and model evaluations.

## Usage
To use this project, follow these steps:
1. Clone the repository: `git clone https://github.com/yourusername/airplane-crash-database.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Configure the database connection in the `config.py` file.
4. Run the data extraction script: `python extract_data.py`
5. Run the analysis and modeling scripts: `python analyze_data.py` and `python model_data.py`

## Contributing
Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
