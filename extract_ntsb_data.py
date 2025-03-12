import requests
import psycopg2
from bs4 import BeautifulSoup

# Database connection
conn = psycopg2.connect("dbname=yourdbname user=youruser password=yourpassword host=yourhost port=yourport")
cur = conn.cursor()

# NTSB Aviation Investigation Search URL
url = "https://www.ntsb.gov/Pages/AviationQueryv2.aspx"

# Function to extract data
def extract_data():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Placeholder for actual extraction logic
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
        
        # Insert data into database
        cur.execute("""
            INSERT INTO airplane_crashes (event_date, location, operator, aircraft_type, registration, flight_number, route, fatalities, description, source_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (event_date, location, operator, aircraft_type, registration, flight_number, route, fatalities, description, source_url))
        conn.commit()

# Run the extraction
extract_data()

# Close the database connection
cur.close()
conn.close()
