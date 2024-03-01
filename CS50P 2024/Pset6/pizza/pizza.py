# Maimoona Aziz

import csv
import sys
from tabulate import tabulate


def main():
    # Get user input via 1 command-line argument and check if arg ends with ".csv"
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # Print formatted table
    menu = sys.argv[1]
    print(format_table(menu))


def format_table(menu):
    # Initialize empty list
    table = []

    # Open menu and use a reader to format it properly
    try:
        with open(menu, "r") as file:
            reader = csv.reader(file)

            # Append row into table
            for row in reader:
                table.append(row)
    # Exit if non-existent
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Return formatted table
    return tabulate(table, headers="firstrow", tablefmt="grid")


main()
