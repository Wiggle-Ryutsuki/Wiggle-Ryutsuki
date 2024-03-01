# Maimoona Aziz

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Check format, if correct extract numbers
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        numbers = matches.groups()

        # Check if each number is within range
        for num in numbers:
            if 0 > int(num) or int(num)> 255:
                return False
        return True
    
    # If not correct, false
    else:
        return False


if __name__ == "__main__":
    main()
