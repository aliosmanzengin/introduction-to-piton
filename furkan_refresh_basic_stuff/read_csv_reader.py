import csv
import json



# Read the CSV file using csv.reader() and manually handle the headers
with open('myFile0.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # Extract the headers (first row)
    headers = next(reader)

    # Construct the list of dictionaries
    data = []
    for row in reader:
        # Create a dictionary by pairing headers with each row's values
        row_dict = dict(zip(headers, row))
        data.append(row_dict)

# Write the list of dictionaries to a JSON file
with open('output_from_reader.json', mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)

print(f"Data successfully written to {'output_from_reader.json'}")
