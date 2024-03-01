# Maimoona Aziz

while True:
    try:
        # Prompt user for a fraction
        fraction = input("Fraction: ")
        parts = fraction.split("/")

        # Check if there are 2 numbers
        if len(parts) != 2:
            continue

        # Split into numerator and denominator
        x = int(parts[0])
        y = int (parts[1])

        # Check if numerator is greater than y
        if x > y:
            continue

        # Calculate fraction into percentage, x / y * 100
        percent = round((x / y) * 100)

    # Catch errors
    except (ValueError, ZeroDivisionError):
        pass

    # If no errors, break out of loop
    else:
        break

# If equal or more than 99, F
if percent >= 99:
    print("F")

# If equal to or less than 1, E
elif percent <= 1:
    print("E")

# Else print percentage
else:
    print(f"{percent}%")
