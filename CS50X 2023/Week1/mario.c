#include <stdio.h>
#include <cs50.h>

int get_size(void);
void print_grid(int n);
int main(void)
{
   //Asking for size
   int n = get_size();

    //Printing grid
    print_grid(n);
}








int get_size(void)
{
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1);
    return n;
}

void print_grid(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("# ");
        }
        printf(" \n");
    }
}







