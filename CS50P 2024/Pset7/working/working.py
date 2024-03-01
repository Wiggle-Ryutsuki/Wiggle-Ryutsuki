# Maimoona Aziz

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Accept only 12 hour format, NEED 2 times, NEED hours, NEED AM | PM, OPTIONAL MINUTES
    if matches := re.search(r"^(([1-9]|1[0-2])(:([0-5][0-9]))? (AM|PM)) to (([1-9]|1[0-2])(:([0-5][0-9]))? (AM|PM))$", s):
        time1 = matches.group(1)
        time2 = matches.group(6)

        # Convert time and return string
        time1_convert = convert_24(time1)
        time2_convert = convert_24(time2)

        return f"{time1_convert} to {time2_convert}"
    else:
        raise ValueError()


# Function that converts 12-hour format into 24-hour format
def convert_24(twelve):
    # Split time into time and period
    try:
        time, period = twelve.split(" ")
        hour, minute = time.split(":")

        # Split time and convert time into int
        hour = int(hour)
        minute = int(minute)
        period = period.lower()

        # If time is PM and less than 12, add 12
        if "pm" in period and hour < 12:
            hour = hour + 12
        # If time is AM and is 12, change time to 0
        elif "am" in period and hour == 12:
            hour = 0

        return f"{hour:02}:{minute:02}"
    except ValueError:
        hour, period = twelve.split(" ")

        hour = int(hour)
        period = period.lower()

        # If time is PM and less than 12, add 12
        if "pm" in period and hour < 12:
            hour = hour + 12
        # If time is AM and is 12, change time to 0
        elif "am" in period and hour == 12:
            hour = 0

        return f"{hour:02}:00"


if __name__ == "__main__":
    main()
