#include <cs50.h>
#include <stdio.h>

int factorial(int number);

int main (void)
{
    // Prompt user for number
    int number = get_int("Enter a number: ");
    printf("%i\n", factorial(number));
}

int factorial(int number)
{
    if (number == 1)
    {
        return 1;
    }
    return number * factorial(number - 1);
}