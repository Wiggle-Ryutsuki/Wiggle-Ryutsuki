# Maimoona Aziz

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        # Prompt for user input
        order = input("Item: ")

        # Convert order to title case
        order = order.title()

        # If item is present in menu
        if order in menu:
            # Add to total
            total += menu[order]
            # Print
            print(f"Total: ${total:.2f}")

        # Else keep prompting
        else:
            continue

    # When CTRL-D is pressed, print total then break out of loop
    except EOFError:
        print(f"\nTotal: {total:.2f}")
        break
