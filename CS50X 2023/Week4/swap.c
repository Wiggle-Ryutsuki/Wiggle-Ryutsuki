#include <stdio.h>

void swap (int *x, int *y);

int main(void)
{
    int x = 1;
    int y = 2;

    printf ("x is %i, y is %i\n", x, y);
    swap(&x, &y);
    printf("- SWAP -\n");
    printf ("x is %i, y is %i\n", x, y);
}

void swap (int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}