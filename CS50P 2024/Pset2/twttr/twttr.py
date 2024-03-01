# Maimoona Aziz

# Initialize vowel list
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

# Ask for input
text = input("Input: ")

# For every letter in the text
for t in text:
    # If letter is not in list of vowels
    if t not in vowels:
        # Print letter
        print(t, end="")
# New line
print()
