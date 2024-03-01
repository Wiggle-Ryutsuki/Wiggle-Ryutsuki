#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    // Gets positive number input from user
    string input = get_string("Enter a positive integer: ");

    // Loop that scans every character in the input and outputs *invalid* if every character isnt a numerical digit
    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // TODO
    if (input[0] == '\0')
    {
        return 0;
    }

    int l = strlen(input);

    //Convert last character to integer
    int last = input[l - 1] - '0';

    // Variable for rest of the string without the last digit

    char remain[l -1 + 1];
    strncpy(remain, input, l - 1);
    remain[l - 1] = '\0';

    return convert(remain) * 10 + last;
}