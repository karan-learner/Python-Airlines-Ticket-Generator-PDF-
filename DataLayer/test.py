import requests
from bs4 import BeautifulSoup
import json

# Wikipedia URL
url = "https://en.wikipedia.org/wiki/List_of_airports_in_India"

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all tables with class 'wikitable'
tables = soup.find_all('table', {'class': 'wikitable'})

areas_served = []

# Loop through each table and extract 'Area served' (first column)
for table in tables:
    rows = table.find_all('tr')[1:]  # Skip header
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 1:
            # Extract from first column (Area Served)
            area_tag = cols[0].find('a')
            area = area_tag.get_text(strip=True) if area_tag else cols[0].get_text(strip=True)
            areas_served.append(area)

# Save to JSON
with open('areas_served.json', 'w') as f:
    json.dump(areas_served, f, indent=4)

print("✅ Extracted and saved 'Area Served' data to areas_served.json")
