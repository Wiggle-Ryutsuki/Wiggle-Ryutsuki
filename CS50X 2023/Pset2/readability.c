// Maimoona Aziz
#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
float average_letters(int words, int letters);
float average_sentence(int words, int sentence);
int grade_level(float a_let, float a_sen);

int main(void)
{
    // Ask for text
    string text = get_string("Text: ");

    int letters = count_letters(text);
    int words = count_words(text);
    int sentence = count_sentences(text);
    float a_let = average_letters(words, letters);
    float a_sen = average_sentence(words, sentence);
    int g_level = grade_level(a_let, a_sen);

    // If it's less than 1
    if (g_level < 1)
    {
        printf("Before Grade 1\n");
    }

    // If it's more than 16
    else if (g_level >= 16)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %i\n", g_level);
    }
}

// Function which counts letters in given text
int count_letters(string text)
{
    int letters = 0;                       // Variable for counting letters
    for (int i = 0; i < strlen(text); i++) // Loop which goes through the text
    {
        // Checks for upper and lowercase letters, no punctuations or numbers
        if (isupper(text[i]) || islower(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

// Function which counts words in a given text
int count_words(string text)
{
    // There's at least 1 word
    int words = 1;                         // Variable for counting words
    for (int j = 0; j < strlen(text); j++) // Loops through text
    {
        // Checks for spaces since words are separated by spaces
        if (isspace(text[j]))
        {
            words++;
        }
    }
    return words;
}

// Function which counts sentences in a given text
int count_sentences(string text)
{
    int sentences = 0;                     // Variable for counting sentences
    for (int k = 0; k < strlen(text); k++) // Loops through text
    {
        // Checks for punctuation (A sentence ends with ".", "?", or "!" but punctuations also have spaces after them)
        if ((text[k] == '.' || text[k] == '?' || text[k] == '!') && (isspace(text[k + 1]) || text[k + 1] == '\0'))
        {
            sentences++;
        }
    }
    return sentences;
}

// Function which counts the average number of letters per 100 words in a text
float average_letters(int words, int letters)
{
    return ((float) letters / words) * 100; // Just returns the variables after computing and stores it in 'a_let'
}

// Funtion which counts the average number of sentences per 100 words in a text
float average_sentence(int words, int sentence)
{
    return ((float) sentence / words) * 100; // Just returns variables after computing and stores it in 'a_sen'
}

// Function which computes the grade-level using the  Coleman-Liau index
int grade_level(float a_let, float a_sen)
{
    // Storing the variables into their appropriate boxes ("L" and "S")
    float index = 0;
    float L = a_let;
    float S = a_sen;

    index = 0.0588 * L - 0.296 * S - 15.8;

    return round(index); // Rounds it then stores the number in g_level
}