import sys

def main():
    menu = {"Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}

    order = []
    total = 0.00

    try:
        while True:
            item = input("Item: ")
            if not item:
                print(f"Total cost: ${total:.2f}")
                continue

            item = item.title()

            if item in menu:
                order.append(item)
                total += menu[item]
                print(f"Total: ${total:.2f}")
            else:
                print("Invalid item")

    except EOFError:
        print("\nOrder summary: ")
        for item in order:
            print(item)
            print(f"Total cost: ${total:.2f}")

if __name__ == "__main__":
    main()