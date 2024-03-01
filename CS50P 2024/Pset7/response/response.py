# Maimoona Aziz

from validator_collection import validators

try:
    validators.email(input("What's your email? "))
    print("Valid")
except ValueError:
    print("Invalid")
