# Maimoona Aziz
import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py DATA.CSV SEQUENCE.TXT")
        sys.exit(1)

    # TODO: Read database file into a variable
    data_file = sys.argv[1]
    data = []  # List that memory will be read into from CSV file

    try: # In case it can't be opened
        with open(data_file, "r") as d_file:
            d_reader = csv.DictReader(d_file)

            for row in d_reader:
                data.append(row)

                pass
    except FileNotFoundError:
        print("File could not be opened")

    # TODO: Read DNA sequence file into a variable
    dna_seq = sys.argv[2]
    dna = []  # List that memory will be read into from DNA sequence file

    try: # In case it can't be opened
        with open(dna_seq, "r") as dna_f:
            dna = dna_f.read()

            pass
    except FileNotFoundError:
        print("File could not be opened 2")

    # TODO: Find longest match of each STR in DNA sequence
    # I need a list of STRs from the first lines from the CSV file
    strs = list(data[0].keys())
    strs.remove("name") # Remove name
    result = {}

    for s in strs:
        longest_run = longest_match(dna, s)
        result[s] = longest_run

    # TODO: Check database for matching profiles
    match_found = False

    for row in data:
        for c_str in strs:
            current = int(row[c_str])
            expected = int(result[c_str])

            if current != expected:
                break

        else:
            match_found = True
            print(row["name"])
            break

    else:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
