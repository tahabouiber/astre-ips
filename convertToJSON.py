import csv
import json

# Define the paths for the input CSV file and the output JSON file
csv_file_path = 'MyData.csv'
json_file_path = 'MyData.json'
csv_file_path = 'Validateur.csv'
json_file_path = 'Validateur.json'

# Read the CSV file and convert it to a JSON format
data = []
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# Write the data to a JSON file
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV has been converted to JSON and saved to {json_file_path}")
