"""
Create a small module of API framework for building request body:
As input you have JSON
As output - body prepared for sending (f.e. For syslog => str)

You need to convert input, according to the chosen format using OOP principles(create more than 3 classes). Take any 3 formats from the list below: , not the same as input (JSON => JSON ):(opens in a new tab)

CSV: Comma Separated Values(opens in a new tab)(opens in a new tab)
SYSLOG: syslog formatted message(opens in a new tab)
KV: key-value pair(opens in a new tab)
XML: Extensible Markup Language(opens in a new tab)
SYSLOG + KV: syslog header with key-value body
SYSLOG + JSON(opens in a new tab): syslog header with JSON body
SYSLOG + XML: syslog header with XML body
LEEF: Log Event Extended Format(opens in a new tab)
CEF: Common Event Format(opens in a new tab)
Note:

In case you want to change input\output format to any other not from the list - agree with a professor (using the same format in input and output format, JSON => JSON, is not allowed)

create a small validation for your input.

If the chosen format doesn’t have layers, set it as text.

Below you can find the example of JSON():
                                        {
                                        "className":"Class 1A",
                                        "year":2022,
                                        "phoneNumber":null,
                                        "active":true,
                                        "homeroomTeacher":{"firstName":"Richard", "lastName":"Roe"},
                                        "members":[
                                        {"firstName":"Jane","lastName":"Doe"},
                                        {"firstName":"Jinny","lastName":"Roe"},
                                        {"firstName":"Johnny","lastName":"Roe"},
                                        ]
                                        }
"""

import json
import csv
import xml.etree.ElementTree as ET


class RequestBody:
    def __init__(self, input_json):
        self.data = json.loads(input_json)

    def validate(self):
        # Simple validation to check if data is a dictionary
        if not isinstance(self.data, dict):
            raise ValueError("Invalid input format. Expecting a JSON object.")


class CSVBody(RequestBody):
    def build(self):
        self.validate()
        output = []
        header = self.data.keys()
        output.append(','.join(header))
        output.append(','.join(map(str, self.data.values())))
        return '\n'.join(output)


class SyslogBody(RequestBody):
    def build(self):
        self.validate()
        return f"<22>1 {self.data['className']} {self.data['year']} {self.data['phoneNumber']} {self.data['active']}"


class KeyValueBody(RequestBody):
    def build(self):
        self.validate()
        return ' '.join([f"{k}={v}" for k, v in self.data.items()])


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

# CSV
csv_body = CSVBody(input_json)
print("CSV Format:")
print(csv_body.build())

# Syslog
syslog_body = SyslogBody(input_json)
print("\nSyslog Format:")
print(syslog_body.build())

# Key-Value
kv_body = KeyValueBody(input_json)
print("\nKey-Value Format:")
print(kv_body.build())
