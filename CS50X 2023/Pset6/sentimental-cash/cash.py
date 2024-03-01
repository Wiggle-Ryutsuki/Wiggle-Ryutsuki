# Maimoona Aziz
# TODO


def main():
    # Prompt user for amount of coins owed
    cents = get_coins()

    # Calculate how many quarters owed
    quarters = cal_quarters(cents)
    cents = cents - quarters * 25
    print(f"Quarters: {quarters}")

    # Calculate how many dimes are owed
    dimes = cal_dimes(cents)
    cents = cents - dimes * 10
    print(f"Dimes: {dimes}")

    # Calculate how many nickels owed
    nickels = cal_nickels(cents)
    cents = cents - nickels * 5
    print(f"Nickels: {nickels}")

    # Calculate how many pennies owed
    pennies = cal_pennies(cents)
    cents = cents - pennies * 1
    print(f"Pennies: {pennies}")

    # Calculate then print total number of coins
    coins = quarters + dimes + nickels + pennies
    print(f"Total coins: {coins}")


# Function that will prompt user for a positive float
def get_coins():
    while True:
        try:
            cents = float(input("Change Owed: "))
            if cents > 0:
                cents = convert(cents)
                break
        except ValueError:
            print("Invalid Value")
    return cents


# Function that converts dollars to cents
def convert(cents):
    cents = cents * 100 # Multiply by 100 to convert dollars to cents
    return int(cents) # Convert to int


# Function that calculates quarters
def cal_quarters(cents):
    # Initialize variable for quarters
    quarters = 0

    # Loop that adds 1 to quarters for everytime it subtracts 25 while cents is still more than 25
    while cents >= 25:
        cents -= 25
        quarters += 1

    return quarters


# Function that calculates dimes
def cal_dimes(cents):
    # Initialize variable for dimes
    dimes = 0

    # Loop that adds 1 to dimes for everytime it subtracts 10 while cents is still more than 10
    while cents >= 10:
        cents -= 10
        dimes += 1

    return dimes


# Function that calculates nickels
def cal_nickels(cents):
    # Initialize variable for nickels
    nickels = 0

    # Loop that adds 1 to nickels for everytime it subtracts 5 while cents is still more than 5
    while cents >= 5:
        cents -= 5
        nickels += 1

    return nickels


# Function that calculates pennies
def cal_pennies(cents):
    # Initialize variable for pennies
    penny = 0

    # Loop that adds 1 to quarters for everytime it subtracts 1 while cents is still more than 1
    while cents >= 1:
        cents -= 1
        penny += 1

    return penny


main()
