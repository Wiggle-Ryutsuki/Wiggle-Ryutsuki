# Prompt user for a greeting
greet = input("Greeting: ")

# Remove leading or trailing whitespace from greeting
greet = greet.strip()

# Convert to lowercase to make it case sensitive
greet = greet.lower()

# If greeting starts with or is hello, output $0
if greet.startswith("hello"):
    print("$0")

# else if greeting starts with h but not "hello" output $20
elif greet.startswith("h"):
    print("$20")

# Else output $100
else:
    print("$100")