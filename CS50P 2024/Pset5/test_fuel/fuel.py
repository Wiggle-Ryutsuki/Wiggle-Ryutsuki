# Maimoona Aziz


def main():
    while True:
        try:
            # Prompt user for a fraction
            fraction = input("Fraction: ")
            # Convert fraction into percentage
            percent = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    # Print percentage or E or F
    print(gauge(percent))


def convert(fraction):
    try:
        # Split parts and convert to int
        parts = fraction.split("/")
        x = int(parts[0])
        y = int(parts[1])
    except ValueError:
        raise

    # Check if Y is 0 or X is larger than Y
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
         raise ValueError

    # Calculate percentage and return
    percent = round((x / y) * 100)

    return percent


def gauge(percentage):
    # If equal or more than 99, F
    if percentage >= 99:
        return "F"

    # If equal to or less than 1, E
    elif percentage <= 1:
        return "E"

    # Else print percentage
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
