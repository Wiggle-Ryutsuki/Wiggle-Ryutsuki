// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(int argc, string argv[]);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Error! Only one word is allowed! \n");
        return 1;
    }
    else
    {
        printf("%s \n", replace(argc, argv));
    }
}

string replace(int argc, string argv[])
{
    string word = argv[1];
    int i = 0;
    while (word[i] != '\0')
    {
        switch (word[i])
        {
            case 'a':
            case 'A':
                word[i] = '6';
                break;
            case 'e':
            case 'E':
                word[i] = '3';
                break;
            case 'i':
            case 'I':
                word[i] = '1';
                break;
            case 'o':
            case 'O':
                word[i] = '0';
                break;
        }
        i++;
    }
    return word;
}