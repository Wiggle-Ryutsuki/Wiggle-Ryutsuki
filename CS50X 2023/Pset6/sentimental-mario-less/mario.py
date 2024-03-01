# Maimoona Aziz
# TODO


def main():
    # Prompt for height more than one and less than 8
    height = 0
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                break
        except ValueError:
            print("Invalid input")

    # print_walls
    print_walls(height)


# function for printing walls
def print_walls(height):
    for high in range(1, height + 1):  # For height
        for space in range(1, height - high + 1):
            print(" ", end="")  # Printing spaces
        for wide in range(1, high + 1):  # For width
            print("#", end="")  # Printing hashes
        print()


main()
