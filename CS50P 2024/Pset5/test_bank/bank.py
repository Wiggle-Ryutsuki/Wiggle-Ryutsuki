# Maimoona Aziz


def main():
    # Ask user for greeting
    greet = input("Greeting: ")
    print(f"${value(greet)}")


def value(greeting):
    # Remove spacings and make all lowercase
    greeting = greeting.lower().strip()

    # Check if it is or starts with "hello", Output $0
    if greeting.startswith("hello"):
        return 0

    # Check if greeting starts with "H" but not "Hello", Output $20
    elif greeting.startswith("h"):
        return 20

    # Else $100
    else:
        return 100

if __name__ == "__main__":
    main()
