import csv
import requests
import sys


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}

    for row in reader:
        state = row["state"]
        case = int(row["cases"])

        if state not in new_cases:
            new_cases[state] = []

        previous_cases = new_cases[state]

        if len(previous_cases) >= 14:
            previous_cases.pop(0)

        if len(previous_cases) == 0:
            new_cases[state].append(case)

        else:
            new_daily = case - previous_cases[-1]
            new_cases[state].append(new_daily)

        previous_cases = new_cases[state]

    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    # If state not in new_cases or length of new_cases[state] is less than 14
    for state in states:
        if state not in new_cases or len(new_cases[state]) < 14:
            # Return error message and exit
            print("Invalid State")
            sys.exit(1)

        # Calculate average

        # last week average = summing new_cases[state][0:7] divide by 7
        last_avg = sum(new_cases[state][0:7]) / 7

        # this week average by summing new_cases[state][7:14] divide by 7
        this_avg = sum(new_cases[state][7:14]) / 7

        # Calculate percant change = subtract last week by this week average and divide by last week then * 100
        try:
            percent_change = ((float(this_avg) - float(last_avg)) / float(last_avg)) * 100
        except ZeroDivisionError:
            print("Error: Division by zero")
            sys.exit(1)


        increase_or_decrease = "increase" if percent_change >= 0 else "decrease"

    # Print the result
    print(f"{state} had a 7-day average of {int(this_avg)} and an {increase_or_decrease} of {(abs(percent_change))}%")


main()
