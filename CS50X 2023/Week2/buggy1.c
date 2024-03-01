#include <stdio.h>
#include <cs50.h>

int get_negative(void);

int main(void)
{
    int i = get_negative();
    printf("%i\n", i);
}

// Prompt user for positive number
int get_negative(void)
{
    int n;
    do
    {
        n = get_int("Negative number: ");
    }
    while (n > 0);
    return n;
}