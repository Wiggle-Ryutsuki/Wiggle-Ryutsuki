# Maimoona Aziz

# Ask user for greeting
greet = input("Greeting: ")

# Remove spacings and make all lowercase
greet = greet.lower().strip()

# Check if it is or starts with "hello", Output $0
if greet.startswith("hello"):
    print("$0")

# Check if greeting starts with "H" but not "Hello", Output $20
elif greet.startswith("h"):
    print("$20")

# Else $100
else:
    print("$100")
