// Practice writing a function to find a max value

#include <cs50.h>
#include <stdio.h>

// function that finds max number
int max(int array[], int n);

int main(void)
{
    // n is the variable that stores HOW MANY numbers are there
    int n;
    do
    {
        // get number of elements
        n = get_int("Number of elements: ");
    }
    while (n < 1);

    // loop that now requests to fill information into the array
    int array[n];
    for (int i = 0; i < n; i++)
    {
        array[i] = get_int("Element %i: ", i);
    }

    printf("The max value is %i.\n", max(array, n));
}

// TODO: return the max value
int max(int array[], int n)
{
    int max = 0;
    for (int i = 1; i < n; i++)
    {
        if (array[max] < array[i])
        {
            max = i;
        }
    }
    return array[max];
}
