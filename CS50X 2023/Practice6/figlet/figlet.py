import sys
import random
from pyfiglet import Figlet

# Check the number of command-line arguments
def main():

    args = sys.argv[1:]

    # if there are 0 arguments, select random
    if len(args) == 0:
        f = random_font()

    # if there are 2 arguments, check if the first one is -f or --font
    elif len(args) == 2 and args[0] in ("-f", "--font"):
        f = args[1]
        figlet = Figlet()
        if f not in figlet.getFonts():
            print("Invalid font")
            sys.exit(1)

    else:
        print("Invalid usage")
        sys.exit(1)

    # prompt user for input
    text = input("Input: ")
    print_font(text, f)


# select a random font
def random_font():

    figlet = Figlet()
    font_list = figlet.getFonts()
    return random.choice(font_list)


# print text in the selected font
def print_font(text, f):

    fig = Figlet(font=f)
    print(fig.renderText(text))


if __name__ == "__main__":
    main()