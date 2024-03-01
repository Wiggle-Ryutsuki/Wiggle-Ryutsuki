# Maimoona Aziz
# TODO

from cs50 import get_string


def main():
    text = get_string("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    avg_let = avg_letters(letters, words)
    avg_sen = avg_sentences(words, sentences)
    g_level = grade_level(avg_let, avg_sen)

    if g_level < 1:
        print("Before Grade 1")

    elif g_level >= 16:
        print("Grade 16+")

    else:
        print(f"Grade {g_level}")


# Function that counts number of LETTERS in given text
def count_letters(text):
    # Variable for counting letters
    letters = 0
    # Loop to go through text
    for c in text:
        # Check if C is an upper or lowercase letter (punctuation and numbers dont have cases hehe)
        if c.islower() or c.isupper():
            # add to letter
            letters += 1

    return letters


# Function that counts number of WORDS in given text
def count_words(text):
    # Python has a function that splits a string into a list of words
    words = text.split()
    return len(words)


# Function that counts number of SENTENCES in given text
def count_sentences(text):
    # Variable to count number of sentences
    sen = 0
    for s in text:
        if s == "." or s == "?" or s == "!":
            sen += 1

    return sen


# Function that calculates AVERAGE number of LETTERS per 100 WORDS in given text
def avg_letters(letters, words):
    avg = (letters / words) * 100

    return avg


# Function that calculates AVERAGE number of SENTENCES per 100 WORDS in given text
def avg_sentences(words, sentences):
    avg = (sentences / words) * 100

    return avg


# Function which computes the grade-level using the  Coleman-Liau index
def grade_level(avg_let, avg_sen):
    index = 0
    L = avg_let
    S = avg_sen

    index = 0.0588 * L - 0.296 * S - 15.8

    return round(index)


main()
