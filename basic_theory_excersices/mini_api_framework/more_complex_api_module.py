import csv
import io
import xml.etree.ElementTree as ET
import json  # <-- Add this line


class RequestBody:
    def __init__(self, input_json):
        self.data = json.loads(input_json)

    def validate(self):
        if not isinstance(self.data, dict):
            raise ValueError("Invalid input format. Expecting a JSON object.")


class ComplexCSVBody(RequestBody):
    def build(self):
        self.validate()
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=self.data.keys())
        writer.writeheader()
        writer.writerow(self.data)
        return output.getvalue()


class XMLBody(RequestBody):
    def build(self):
        self.validate()
        root = ET.Element("root")
        for key, value in self.data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        return ET.tostring(root, encoding="unicode")


# Test the classes
input_json = json.dumps({
    "className": "Class 1A",
    "year": 2022,
    "phoneNumber": None,
    "active": True,
    "homeroomTeacher": {"firstName": "Richard", "lastName": "Roe"},
    "members": [
        {"firstName": "Jane", "lastName": "Doe"},
        {"firstName": "Jinny", "lastName": "Roe"},
        {"firstName": "Johnny", "lastName": "Roe"},
    ]
})

# Complex CSV using csv module
complex_csv_body = ComplexCSVBody(input_json)
print("Complex CSV Format using csv module:")
print(complex_csv_body.build())

# XML using xml.etree.ElementTree
xml_body = XMLBody(input_json)
print("\nXML Format using xml.etree.ElementTree:")
print(xml_body.build())
