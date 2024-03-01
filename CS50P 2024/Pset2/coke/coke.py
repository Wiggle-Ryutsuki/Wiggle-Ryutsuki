# Maimoona Aziz

# Declare initial amount
amount = 50

# Ask user for input (only for 25, 10, 5)
while True:
    # Declare amount due
    print(f"Amount Due: {amount}")
    # Ask for user input
    coin = int(input("Insert Coin: "))

    # If 25, 10, or 5, proceed
    if coin == 25 or coin == 10 or coin == 5:

        # Calculate new amount
        amount = amount - coin

        # Check if 0 or negative
        if amount <= 0:
            # Print change then end
            print(f"Change Owed: {abs(amount)}")
            break
    # Keep looping
