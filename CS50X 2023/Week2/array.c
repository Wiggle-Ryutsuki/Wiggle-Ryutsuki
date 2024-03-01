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

    int doubles;
    doubles = 1;
    printf("%i \n", doubles);

    for (int i = 1; i < length; i++)
    {
        doubles = doubles * 2;
        printf("%i \n", doubles);
    }
}