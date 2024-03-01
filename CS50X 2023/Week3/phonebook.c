#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
people;

int main(void)
{
    people person[2];

    person[0].name = "Carter";
    person[0].number = "+1-617-495-1000";

    person[1].name = "David";
    person[1].number = "+1-949-468-2750";

    string name = get_string("Name: ");
    for (int i = 0; i < 2; i++)
    {
        if (strcmp(person[i].name, name) == 0)
        {
            printf("Found %s\n", person[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}