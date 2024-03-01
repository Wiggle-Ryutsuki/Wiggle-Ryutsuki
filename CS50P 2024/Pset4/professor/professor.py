# Maimoona Aziz

import random


def main():
    # Get level
    level = get_level()

    # Set i to 0 (for looping)
    i = 0
    # set score to 0
    score = 0

    # Loop until 10
    while i != 10:
        # Get numbers
        x, y = generate_integer(level)
        # Calculate sum to numbers
        z = x + y

        # Set error to 0
        error = 0

        # While errors are less than 3
        while error < 3:
            try:
                # Prompt user for answer
                ans = int(input(f"{x} + {y} = "))

                # If correct, add score and next question
                if ans == z:
                    score += 1
                    break
                # Else error message and prompt again
                else:
                    print("EEE")
                    error += 1
            except ValueError:
                pass

        # If error = 3, print answer
        if error == 3:
            print(f"{x} + {y} = {z}")
        # Increment loop
        i += 1

    # Print score at the end
    print(f"Score: {score}")


def get_level():
    # Loop
    while True:
        try:
            # Get input
            level = int(input("Level: "))
            # If input not 1, 2, or 3, keep prompting
            if level not in [1, 2, 3]:
                continue
        except ValueError:
            pass
        else:
            # Return level
            return level


def generate_integer(level):
    # If level is more than lower bound is 10 ^ (level - 1)
    if level > 1:
        lower = 10**(level-1)
    # if level is 1, lower bound is 0
    else:
        lower = 0

    # Get random numbers with range of [level] digits
    x = random.randint(lower, 10**level - 1)
    y = random.randint(lower, 10**level - 1)

    # Return x and y
    return x, y

if __name__ == "__main__":
    main()
