# Maimoona Aziz

import sys


def main():
    # Get user input via 1 command-line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if arg ends with ".py"
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    print(count_file())


def count_file():
    lines = 0
    # Open file
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                # Check if line is a comment and if line is blank
                line = line.lstrip()
                stripped_line = line.strip()
                if stripped_line and not line.startswith("#"):
                    lines += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    # Return number of lines found
    return lines


main()
