#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Prompt for Name
    string name = get_string("Name: ");
    //Prompt for Age
    int age = get_int("Age: ");
    //Prompt for Phone number
    string num = get_string("Phone number: ");
    //Output all of the Information
    printf("Name: %s \n Age: %i \n Phone number: %s \n ", name, age, num);
}