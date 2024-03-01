// Maimoona Aziz
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO: Scan and check if the name input is valid || Add 1 to candidates.votes for every valid vote

    // Loops over number of candidates
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0) // Checks if name matches any of the valid candidates
        {
            candidates[i].votes += 1; // When yes, add 1 to votes
            return true;
        }
    }
    return false; // False if no (aka name not valid). Then up in main it outputs "Invalid Vote!"
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO: Scan for the biggest number || Print out all the names with the biggest number

    int win = 0; // Variable which will keep track of the biggest number of votes

    // This loop finds the biggest number of votes
    // Loops through number of candidates
    for (int i = 1; i < candidate_count; i++)
    {
        if (candidates[win].votes < candidates[i].votes) // Compares current "big number" with the next number
        {
            win = i; // Changes if other number is bigger
        }
    }

    // This loop will print out all the candidates with the largest number of votes
    // Loops through number of candidates
    for (int j = 0; j < candidate_count; j++)
    {
        // Finds all the candidates which have "the largest number of votes" aka [win]
        if (candidates[j].votes == candidates[win].votes)
        {
            printf("%s\n", candidates[j].name); // Prints candidate
        }
    }
    return;
}