# Maimoona Aziz

def main():
    # Get time
    time = input("What time is it? ")

    # Call convert to convert time
    t = float(convert(time))

    # Check if time is between 7:00 and 8:00 (breakfast)
    if 7 <= t and t <= 8:

        print("Breakfast time")

    # Check if time is between 12:00 and 13:00 (lunch)
    elif 12 <= t and t <= 13:

        print("Lunch time")

    # Check if time is between 18:00 and 19:00 (dinner)
    elif 18 <= t and t <= 19:

        print("Dinner time")


# Converts str 24-hour time  to the corresponding number of hours as a float
def convert(time):
    # Converts time into lowercase and removes punctuation incase of 12-hour format
    time = time.lower().replace(".", "")

    # Check if 12-hour format
    if "am" in time or "pm" in time:
        time = convert_24(time) # Convert into 24-hour format

    # Split time into hours and minutes
    hour, minute = time.split(":")

    # Convert to float
    hour = float(hour)
    minute = float(minute)

    # Convert minute to hours
    minute = minute / 60

    # Add hours and minutes
    t = hour + minute

    return t


# Function that converts 12-hour format into 24-hour format
def convert_24(twelve):
    # Split time into time and period
    time, period = twelve.split(" ")
    hour, minute = time.split(":")

    # Split time and convert time into int
    hour = int(hour)
    minute = int(minute)

    # If time is PM and less than 12, add 12
    if "pm" in period and hour < 12:
        hour = hour + 12

    # If time is AM and is 12, change time to 0
    elif "am" in period and hour == 12:
        hour = 0

    return "{}:{}".format(hour, minute)


if __name__ == "__main__":
    main()
