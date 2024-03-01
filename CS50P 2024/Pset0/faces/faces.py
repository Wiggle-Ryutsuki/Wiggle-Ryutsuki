# Maimoona Aziz

def main():
    # Get user input
    words = input("User Input: ")
    words = emoji(words)
    print(words)

# Function that converts :) and :( into emojis
def emoji(input):
    # Check if input is :)
    if ":)" in input:
        input = input.replace(":)", "🙂")
    if ":(" in input:
        input = input.replace(":(", "🙁")
    return (input)

main()
