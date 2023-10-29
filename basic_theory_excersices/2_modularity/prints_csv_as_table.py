"""
Create a script that prints csv text with a header and prints it as a table. Please use PrettyTable library to print it.
Example:
         print_csv("a,b\n1,2")
        +---+---+
        | a | b |
        +---+---+
        | 1 | 2 |
        +---+---+
"""

from prettytable import PrettyTable


def print_csv(csv_text):

    lines = csv_text.strip().split("\n")
    header = lines[0].split(",")
    rows = [line.split(",") for line in lines[1:]]

    # Create a PrettyTable object and set its field names to the CSV header
    table = PrettyTable()
    table.field_names = header

    # Add the rows to the table
    for row in rows:
        table.add_row(row)

    # Print the table
    print(table)


# Test the function with an example
print_csv("a,b\n1,2")

