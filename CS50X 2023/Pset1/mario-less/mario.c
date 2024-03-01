// Maimoona Aziz
// Mario less confident
#include <cs50.h>
#include <stdio.h>

void print_walls(int height);
int main(void)
{
    // Ask for height ; keep asking if value less than 1 and more than 8
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Print out # pyramid
    print_walls(height);
}

// Function for building pyramid
void print_walls(int height)
{
    for (int high = 1; high <= height; high++)
    {
        // Print spaces (spaces are total height - current row)
        for (int space = 1; space <= (height - high); space++)
        {
            printf(" ");
        }

        // Print # pyramid
        for (int wide = 1; wide <= high; wide++)
        {

            printf("#");
        }

        // Next line (row)
        printf("\n");
    }
}