# Maimoona Aziz

import random
import sys
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    arg = sys.argv[1:]

    # Check if command-line arguments = 0 (random)
    if len(arg) == 0:
        f = select_random_font()

    # Check if comand-line arguments = 2 and has "-f" or "--font"
    elif len(arg) == 2 and arg[0] in ["-f", "--font"]:
        f = arg[1]
        # Check if inputted font is available
        if f not in figlet.getFonts():
            sys.exit("Invalid font")

    # Exit
    else:
        sys.exit("Invalid usage")

    # Ask for user input
    text = input("Input: ")

    # Set font then print
    figlet.setFont(font=f)
    print(figlet.renderText(text))


# Function that selects random font
def select_random_font():
    figlet = Figlet()
    # Get list of fonts
    font_list = figlet.getFonts()

    # Return random font
    return random.choice(font_list)

main()
