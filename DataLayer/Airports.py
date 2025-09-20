import json
import os

# Build the correct path to the JSON file inside the JSON subfolder
file_path = os.path.join(os.path.dirname(__file__), 'JsonData', 'airports.json')

# Load the data
with open(file_path, 'r') as file:
    cities = json.load(file)


