//Maimoona Aziz
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Asks for name then stores info
    string name = get_string("What's your name? ");
    //Prints out name
    printf("Hello, %s! \n", name);
}