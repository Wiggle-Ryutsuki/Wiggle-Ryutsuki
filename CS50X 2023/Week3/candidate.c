#include <cs50.h>
#include <stdio.h>

typedef struct
{
    string name;
    int votes;
}
candidate;

candidate get_candidate(string prompt);

int main(void)
{
    candidate candidates_array[3];
    for (int i = 0; i < 3; i++)
    {
        candidates_array[i] = get_candidate("Enter a candidate: ");
    }
    for (int i = 0; i < 3; i++)
    {
        printf("%)
    }
}

candidate get_candidate(string prompt)
{
    printf("%s\n", prompt);

    candidate c;
    c.name = get_string("Name: ");
    c.votes = get_int("Number of votes: ");

    return c;
}