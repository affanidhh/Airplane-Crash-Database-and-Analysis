# Airplane Crash Database and Analysis

This project aims to create a comprehensive database of airplane crashes and perform statistical analysis and predictive modeling to understand the factors contributing to these incidents.

## Table of Contents
- [Introduction](#introduction)
- [Data Sources](#data-sources)
- [Database Schema](#database-schema)
- [Data Extraction](#data-extraction)
- [Data Analysis and Modeling](#data-analysis-and-modeling)
- [Predictive Model Specification](#predictive-model-specification)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Air travel remains one of the safest modes of transportation, but incidents and accidents still occur. This project aims to create a detailed database of airplane crashes, analyze the data to identify patterns and trends, and develop predictive models to help understand the factors that contribute to these accidents.

## Data Sources
The primary sources of data for this project are:
- [National Transportation Safety Board (NTSB)](https://www.ntsb.gov/Pages/AviationQueryv2.aspx)
- [Aviation Safety Network (ASN)](https://asn.flightsafety.org/)
- [Bureau d'Enquêtes et d'Analyses (BEA)](https://www.bea.aero/en/investigation-reports/list-of-reports)
- [Air Accidents Investigation Branch (AAIB)](https://www.gov.uk/government/organisations/air-accidents-investigation-branch)
- [Bundesstelle für Flugunfalluntersuchung (BFU)](https://www.bfu-web.de/EN/Publications/Investigation-Report)
- [European Union Aviation Safety Agency (EASA)](https://www.easa.europa.eu/document-library/accident-reports)

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
Data is extracted from the NTSB, ASN, BEA, AAIB, BFU, and EASA websites using web scraping techniques and stored in the `airplane_crashes` table. The extraction script is written in Python and uses the `requests` and `beautifulsoup4` libraries.

### Script for Data Extraction

```python name=extract_data.py
import requests
import psycopg2
from bs4 import BeautifulSoup

# Database connection
conn = psycopg2.connect("dbname=yourdbname user=youruser password=yourpassword host=yourhost port=yourport")
cur = conn.cursor()

# Function to extract data from a given URL
def extract_data_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    crashes = []
    for item in soup.find_all('div', class_='accident-item'):
        event_date = item.find('span', class_='event-date').text
        location = item.find('span', class_='location').text
        operator = item.find('span', class_='operator').text
        aircraft_type = item.find('span', class_='aircraft-type').text
        registration = item.find('span', class_='registration').text
        flight_number = item.find('span', class_='flight-number').text
        route = item.find('span', class_='route').text
        fatalities = int(item.find('span', class_='fatalities').text)
        description = item.find('span', class_='description').text
        source_url = url
        
        crash = {
            "event_date": event_date,
            "location": location,
            "operator": operator,
            "aircraft_type": aircraft_type,
            "registration": registration,
            "flight_number": flight_number,
            "route": route,
            "fatalities": fatalities,
            "description": description,
            "source_url": source_url
        }
        crashes.append(crash)
    
    return crashes

# List of URLs to extract data from
urls = [
    "https://www.ntsb.gov/Pages/AviationQueryv2.aspx",
    "https://www.bea.aero/en/investigation-reports/list-of-reports",
    "https://www.gov.uk/government/organisations/air-accidents-investigation-branch",
    "https://www.bfu-web.de/EN/Publications/Investigation-Report",
    "https://www.easa.europa.eu/document-library/accident-reports"
]

# Extract data from each URL and insert into the database
for url in urls:
    crashes = extract_data_from_url(url)
    for crash in crashes:
        cur.execute("""
            INSERT INTO airplane_crashes (event_date, location, operator, aircraft_type, registration, flight_number, route, fatalities, description, source_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (crash['event_date'], crash['location'], crash['operator'], crash['aircraft_type'], crash['registration'], crash['flight_number'], crash['route'], crash['fatalities'], crash['description'], crash['source_url']))
        conn.commit()

# Close the database connection
cur.close()
conn.close()
```

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

## Predictive Model Specification

````markdown name=model_specification.md
# Predictive Model for Airplane Crashes

## Introduction
This document outlines the detailed specification of a predictive model designed to forecast the likelihood of airplane crashes based on historical data. The model aims to identify the factors that contribute to airplane crashes and predict future incidents.

## Data
The data used for this model is sourced from the National Transportation Safety Board (NTSB) and the Aviation Safety Network (ASN). The dataset includes detailed information about airplane crashes, such as the date, location, operator, aircraft type, and number of fatalities.

## Data Preprocessing
Before building the model, the data undergoes several preprocessing steps:
1. **Data Cleaning**: Removing or imputing missing values, correcting data types, and handling outliers.
2. **Feature Engineering**: Creating new features from existing data, such as the time of year, weather conditions, and aircraft age.
3. **Data Normalization**: Scaling numerical features to ensure they have similar ranges.

## Model Selection
Several machine learning algorithms will be evaluated to find the best model for predicting airplane crashes. These algorithms include:
1. **Logistic Regression**: A simple yet effective model for binary classification problems.
2. **Random Forest**: An ensemble method that combines multiple decision trees to improve accuracy.
3. **Gradient Boosting**: Another ensemble method that builds models sequentially to correct errors made by previous models.
4. **Support Vector Machine (SVM)**: A powerful classifier that finds the optimal hyperplane to separate classes.

## Model Training
The dataset is split into training and testing sets. The training set is used to train the model, and the testing set is used to evaluate its performance. Cross-validation is performed to ensure the model generalizes well to unseen data.

## Model Evaluation
The model's performance is evaluated using the following metrics:
1. **Accuracy**: The proportion of correctly predicted instances.
2. **Precision**: The proportion of true positive predictions among all positive predictions.
3. **Recall**: The proportion of true positive predictions among all actual positives.
4. **F1-Score**: The harmonic mean of precision and recall, providing a balance between the two.

## Hyperparameter Tuning
Hyperparameter tuning is performed to optimize the model's performance. Techniques such as Grid Search and Random Search are used to find the best combination of hyperparameters for each algorithm.

## Results
The final model is selected based on its performance on the testing set. The results are presented in terms of accuracy, precision, recall, and F1-score. Visualizations such as confusion matrices and ROC curves are used to illustrate the model's performance.

## Conclusion
The predictive model provides valuable insights into the factors contributing to airplane crashes and helps forecast future incidents. The model can be used by aviation authorities and airlines to improve safety measures and prevent future crashes.

## Future Work
Future improvements to the model may include:
1. **Incorporating more features**: Adding additional data such as weather conditions, maintenance records, and pilot experience.
2. **Improving data quality**: Enhancing the dataset by obtaining more accurate and comprehensive data.
3. **Exploring advanced algorithms**: Investigating more sophisticated machine learning techniques such as deep learning.

## Usage
To run the predictive model, follow these steps:
1. Ensure the dataset is preprocessed and cleaned.
2. Split the dataset into training and testing sets.
3. Train the model using the training set.
4. Evaluate the model using the testing set.
5. Perform hyperparameter tuning to optimize the model's performance.
6. Use the final model to make predictions and analyze the results.

## License
This model specification is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
