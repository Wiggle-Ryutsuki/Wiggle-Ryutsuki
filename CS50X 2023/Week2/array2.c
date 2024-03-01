#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Ask for positive integer size
    int length;
    do
    {
        length = get_int("Length: ");
    }
    while (length < 1);

    // Print out array

    // declare array variable
    int doubles[length];
    doubles[0] = 1;
    printf("%i\n", doubles[0]);

    // print out current element which is 2x before value
    for (int i = 1; i < length; i++)
    {
        doubles[i] = 2 * doubles[i - 1];

        printf("%i\n", doubles[i]);
    }
}
