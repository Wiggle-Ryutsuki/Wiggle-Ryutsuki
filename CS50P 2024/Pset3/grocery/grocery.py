# Maimoona Aziz

groceries = {}

while True:
    try:
        # Prompt for user input
        item = input()

        # Convert to uppercase
        item = item.upper()
        # If item is present in menu
        if item in groceries:
            # Increment
            groceries[item] += 1
        # Else keep prompting
        else:
            groceries[item] = 1

    # When CTRL-D is pressed, print total then break out of loop
    except EOFError:

        # For each object in the sorted dictionary, print value than key
        for i in sorted(groceries):
            print(groceries[i], i)
        break
