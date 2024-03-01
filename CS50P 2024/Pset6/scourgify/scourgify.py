# Maimoona Aziz

import csv
import sys


def main():
    # Get user input via 2 command-line arguments and check if arg ends with ".csv"
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    before = sys.argv[1]
    after = sys.argv[2]

    process(before, after)


def process(before, after):
    try:
        # Open before file and read contents || initialize fieldnames
        with open(before, "r") as read_file:
            reader = csv.DictReader(read_file)
            field = ["first", "last", "house"]

            # Open writer to write into after file
            with open(after, "w") as write_file:
                writer = csv.DictWriter(write_file, fieldnames=field)
                writer.writeheader()

                # Split first and last name and write
                for row in reader:
                    last, first = row["name"].split(", ")
                    row = {"first": first, "last": last, "house": row["house"]}
                    writer.writerow(row)
    # Exit if non-existent
    except FileNotFoundError:
        sys.exit("File does not exist")


main()
