# Maimoona Aziz

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_char_limits(s) and check_least_two_letters(s) and check_numbers(s) and check_punct(s) == True:
        return True
    else:
        return False


# Max 6 characters and min 2 characters
def check_char_limits(s):
    # Length over 6 and under 2 = false
    if len(s) > 6 or  len(s) < 2:
        return False
    return True


# First 2 characters must be at least 2 letters
def check_least_two_letters(s):
    # If first 2 characters are not alphabets, false
    if not s[0:2].isalpha():
        return False
    return True


# Numbers must not start with "0" and must not be between letters
def check_numbers(s):
    # For each character
    for i in range(len(s)):
        # If a digit is found
        if s[i].isdigit():
            # If digit is 0, false
            if s[i] == "0":
                return False
            # If digit is not 0, check if rest of the string after digit is digit, if not, false
            elif not s[i:].isdigit():
                return False
            break
    return True


# Must not have punctuation
def check_punct(s):
    # If string is not only alphabet and numbers, false
    if not s.isalnum():
        return False
    return True


if __name__ == "__main__":
    main()
