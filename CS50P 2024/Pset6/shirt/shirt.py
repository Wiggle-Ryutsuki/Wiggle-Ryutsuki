# Maimoona Aziz

import sys
from PIL import Image, ImageOps
import os


def main():
    # Get user input via 2 command-line arguments and check if arg ends with ".jpg" or ".jpeg", or ".png" and if arg1 and arg2 have the same extension
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png", ".JPG")) and sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png"))):
        sys.exit("Invalid input")

    # Assign variables
    before = sys.argv[1].lower()
    after = sys.argv[2].lower()

    # Get extensions then check if extensions are the same
    ext1 = os.path.splitext(before)[1]
    ext2= os.path.splitext(after)[1]

    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    # Apply shirt
    shirtify(before, after)


def shirtify(before, after):
    try:
        # Open image
        image = Image.open(before)
        shirt = Image.open("shirt.png")

        # Get size and crop image
        size = shirt.size
        fitted = ImageOps.fit(image, size)

        # Paste and save
        fitted.paste(shirt, shirt)
        fitted.save(after)

    except FileNotFoundError:
        sys.exit("File does not exist")


main()
