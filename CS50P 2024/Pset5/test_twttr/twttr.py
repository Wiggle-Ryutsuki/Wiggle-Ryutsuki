# Maimoona Aziz

# Initialize vowel list
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

def main():
    # Ask for input
    text = input("Input: ")
    # Print string
    print(shorten(text))

def shorten(word):
    # Initialize an empty string
    new_word = ""
    # For every letter in the text
    for t in word:
        # If letter is not in list of vowels
        if t not in vowels:
            # Add letters to string
            new_word += t
    # Return string
    return f"{new_word}"


if __name__ == "__main__":
    main()
