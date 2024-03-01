# Maimoona Aziz

import requests
import sys
import json

# Exit if no command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Convert n into float, if can't, error
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# Request data and then convert to json, extract rate_float
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    value = float(data["bpi"]["USD"]["rate_float"])
except requests.RequestException:
    sys.exit("error fetching data")

# Calculate cost and print
cost = n * value
print(f"${cost:,.4f}")
