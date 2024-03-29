// Maimoona Aziz
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet (That means the values of the letters should be 0, 1, 2, 3...etc)
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins! \n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins! \n");
    }
    else
    {
        printf("Tie! \n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int score = 0;                                          // Score variable
    for (int i = 0, length = strlen(word); i < length; i++) // Will loop until the end of the word
    {
        if (isupper(word[i])) // For uppercase (keeps adding score to each letters point value || the value of the letters are
                              // subtracted to start from 0, 1, 2, 3..etc)
        {
            score = score + POINTS[word[i] - 'A'];
        }
        else if (islower(word[i])) // For lowercase (keeps adding score to each letters point value || the value of the letters are
                                   // subtracted to start from 0, 1, 2, 3..etc)
        {
            score = score + POINTS[word[i] - 'a'];
        }
    }
    return score;
}
