#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int a = 28;
    int b = 50;
    int *c = &a;

    *c = 14;
    c = &b;
    *c = 25;

    printf("a has value %i at loaction %p\n", a, &a);
    printf("b has value %i at loaction %p\n", b, &b);
    printf("c has value %p at location %p\n", c, &c);
}