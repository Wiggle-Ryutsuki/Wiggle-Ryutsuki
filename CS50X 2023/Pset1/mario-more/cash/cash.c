// Maimoona Aziz
// Cash 
#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;
    printf("Quarters: %i \n", quarters); // Tells me (or cashier) how many quarters

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;
    printf("Dimes: %i \n", dimes); // Tells me (or cashier) how many dimes

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;
    printf("Nickels: %i \n", nickels); // Tells me (or cashier) how many nickels

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;
    printf("Pennies: %i \n", pennies); // Tells me (or cashier) how many pennies

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("Total coins: %i\n", coins);
}

int get_cents(void)
{
    // TODO: Function that asks for cents and stores information (positive only)
    int cents;
    do
    {
        cents = get_int("Cents owed: ");
    }
    while (cents < 0);
    return cents;
}

int calculate_quarters(int cents)
{
    // TODO: Calculate number of quarters
    int quarters;                               // Quarter variable which will count amount of quarters
    for (quarters = 0; cents >= 25; quarters++) // While cents is more than 25, keep calculating
    {
        cents = cents - 25; // Decrease amount by quarter, then add loop count to quarter variable
    }
    return quarters;
}

int calculate_dimes(int cents)
{
    // TODO: Calculate number of dimes
    int dimes;                            // Dime variable which will count amount of dimes
    for (dimes = 0; cents >= 10; dimes++) // While cents is more than 10, keep calculating
    {
        cents = cents - 10; // Decrease amount by dime, then add loop count to dime variable
    }
    return dimes;
}

int calculate_nickels(int cents)
{
    // TODO: Calculate number of nickels
    int nickels;                             // Nickel variable which will count amount of nickels
    for (nickels = 0; cents >= 5; nickels++) // While cents is more than 5, keep calculating
    {
        cents = cents - 5; // Decrease amount by nickel, then add loop count to nickel variable
    }
    return nickels;
}

int calculate_pennies(int cents)
{
    // TODO: Calculate number of pennies
    int penny;                           // Penny variable which will count amount of pennies
    for (penny = 0; cents >= 1; penny++) // While loop count is more than 1, keep calculating
    {
        cents = cents - 1; // Decrease amount by penny, then add loop to penny variable
    }
    return penny;
}
