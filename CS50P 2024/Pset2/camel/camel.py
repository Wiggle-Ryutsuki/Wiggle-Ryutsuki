# Maimoona Aziz

# Prompt user for camel case input
camel = input("camelCase: ")

# For each letter
for c in camel:
    # If uppercase letter found
    if c.isupper():
        # Print "_" and then lowercase letter
        print("_" + c.lower(), end="")
    else:
        # Print letters
        print(c, end="")
# Print new line at the end
print()
