// Maimoona Aziz
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // TODO: Scan and check if the name input is valid || Add the candidate index to preferences for every valid vote

    // Loops over number of candidates
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0) // Checks if name matches any of the valid candidates
        {
            preferences[voter][rank] = i; // Update preferences
            return true;
        }
    }
    return false; // False if no (aka name not valid). Then up in main it outputs "Invalid Vote!"
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // TODO: Check if candidate is eliminated || if not, add votes of highest preference

    for (int i = 0; i < voter_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            int can_index = preferences[i][j];
            if (candidates[can_index].eliminated == false)
            {
                candidates[can_index].votes++;
                break;
            }
        }
    }
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    // TODO: Find half of votes, compare half with all candidates (if candidate > half), if match, print and return true

    // half = round(total / 2.0);
    int half = round(voter_count / 2.0);

    for (int i = 0; i < candidate_count; i++)
    {
        // Finds if a valid candidate is more than half
        if (candidates[i].eliminated == false && candidates[i].votes > half)
        {
            printf("%s\n", candidates[i].name); // Prints candidate
            return true;
        }
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO: find minimum number

    int min = 0; // Variable that will keep tack of minimum number
    for (int i = 1; i < candidate_count; i++)
    {
        // If [current mininum] uneliminated candidate is more than next uneliminated candidate
        if (candidates[i].eliminated == false && candidates[min].votes > candidates[i].votes)
        {
            // Change min to other candidate
            min = i;
        }
    }
    return candidates[min].votes;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // TODO: Compare all votes to minimum vote, if ALL OF THEM are minimum, return true
    // Approach: Look for the votes are NOT MINIMUM, if all of them pass, return true

    for (int i = 0; i < candidate_count; i++)
    {
        // If candidate vote is not equal to minimum AND has not been eliminated
        if (candidates[i].eliminated == false && candidates[i].votes != min)
        {
            // Return false
            return false;
        }
    }
    // All clear! Return true
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO: Find all uneliminated candidates with minimum votes and set eliminate to true

    for (int i = 0; i < candidate_count; i++)
    {
        // If candidate vote = minimum vote AND has not been eliminated
        if (candidates[i].votes == min && candidates[i].eliminated == false)
        {
            // Set eliminate to true
            candidates[i].eliminated = true;
        }
    }
}