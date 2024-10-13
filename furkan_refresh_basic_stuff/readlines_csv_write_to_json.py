import json


# Step 1: Reading the CSV file
with open('myFile0.csv', 'r', newline='', encoding='utf-8') as csv_file:
    lines = csv_file.readlines()  # Read all lines in the CSV file

    # Extract headers from the first line
    headers = lines[0].strip().split(',')
    # split ile ilk satiri stringden liste ceviriyor asagidaki satirdaki gibi gorunecek header
    # [id,firstname,lastname,email,email2,profession]

    # Initialize an empty list to store rows as dictionaries
    data_list = []

    # Step 2: Iterate through the remaining lines (rows) of the CSV
    for line in lines[1:]:  # Skip the header row (lines[0])
        row_values = line.strip().split(',')  # Split each row into values
        row_dict = dict(zip(headers, row_values))  # Create a dictionary for each row
        data_list.append(row_dict)  # Append the dictionary to the data list

# Step 3: Writing the data to a JSON file
with open('myjsonfile.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, indent=4)

print(f"CSV data successfully written to {'myjsonfile.json'}")
