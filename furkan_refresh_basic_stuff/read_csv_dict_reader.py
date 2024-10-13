import csv
import json

# File paths

# Read the CSV file and store the data in a list of dictionaries
data = []
with open('myFile0.csv', mode='r', newline='', encoding='utf-8') as my_csvfile:
    my_reader = csv.DictReader(my_csvfile)
    for row in my_reader:
        data.append(row)

# Write the list of dictionaries to a JSON file
with open('json_file_path', mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)

print(f"Data successfully written to {json_file_path}")
