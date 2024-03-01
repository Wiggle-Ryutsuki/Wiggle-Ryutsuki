# Maimoona Aziz

import random

while True:
    try:
        # Prompt for user level input
        level = int(input("Level: "))

        # If number negative or is not number, keep prompting
        if level < 1:
            continue

    except ValueError:
        pass
    else:
        break

# Pick random number from 1 to number
x = random.randint(1, level)

while True:
    try:
        # Prompt user to guess number
        guess = int(input("Guess: "))

        # If number smaller than number, print "Too small"
        if guess < x:
            print("Too small!")
            continue

        # If number larger than number, print "Too large"
        elif guess > x:
            print("Too large!")
            continue

        # If guessed correctlyy, print "Just right"
        elif guess == x:
            print("Just right!")
            break

    except ValueError:
        pass
