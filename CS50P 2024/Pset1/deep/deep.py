# Maimoona Aziz

# Ask for user input
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Make answer all lowercase and remove spaces
answer = answer.lower().strip()
# Check if answer is 42
match answer:
    # Output "yes" if "42" or "forty two" or "forty-two"
    case "42" | "forty-two" | "forty two":
        print("Yes")

    # Output "no" if not
    case _:
        print("No")
