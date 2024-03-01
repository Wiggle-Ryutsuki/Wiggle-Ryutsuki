# Maimoona Aziz

from datetime import date
import inflect
import re
import sys


def main():
    # Prompt for date
    birth = input("Date of Birth: ")

    # Validate format and convert to date format (also validates date in the process)
    try:
        year, month, day = validate_format(birth)
        birth_date = date(int(year), int(month), int(day))
    except:
        sys.exit("Invalid date")

    # Get current day
    today = date.today()
    # Get minutes
    minutes = calculate_minutes(birth_date, today)

    # Convert to sentence and print
    print(convert_words(minutes), "minutes")


def validate_format(birth):
    # Validate format (4 digit, 2 digit, 2 digit)
    if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", birth):
        # Split year, month, and day
        year = (match.group(1))
        month = (match.group(2))
        day = (match.group(3))

        return year, month, day


def calculate_minutes(birth_date, today):
    # Calculate difference
    diff = today - birth_date
    # Convert it to only Day
    days = diff.days

    return days * 24 * 60


def convert_words(minutes):
    # Convert numbers to sentence, capitalize and then return
    p = inflect.engine()
    sentence = p.number_to_words(minutes,  andword="")

    return sentence.capitalize()


if __name__ == "__main__":
    main()
