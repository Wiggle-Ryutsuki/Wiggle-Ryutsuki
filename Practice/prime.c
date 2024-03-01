#include <cs50.h>
#include <stdio.h>

//Function
bool prime(int number);

int main(void)
{
    //Asking for a positive minumum number
    int min;
    do
    {
        min = get_int("Minimum: ");
    }
    while (min < 1);


    //Asking for a maximum number more than or equal to minimum number
    int max;
    do
    {
        max = get_int("Maximum: ");
    }
    while (min >= max);

    //Loop (Keeps printing primes until min is equal to max)
    for (int i = min; i <= max; i++)
    {
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

bool prime(int number)
{
     // TODO
    if (number <= 1)
    {
        return false;
    }
    for (int i = 2; i * i <= number; i++)
    {
        if (number % i == 0)
        return false;
    }

    return true;
}



