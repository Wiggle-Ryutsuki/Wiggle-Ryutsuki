// Calculate your half of a restaurant bill
// Data types, operations, type casting, return value

#include <cs50.h>
#include <stdio.h>

float half(float bill, float tax, int tip);

int main(void)
{
    //Asking for bill amount
    float bill_amount = get_float("Bill before tax and tip: ");
    //Asking for Sale tax percent
    float tax_percent = get_float("Sale Tax Percent: ");
    //Asking for Tip percent
    float tip_percent = get_int("Tip Percent: ");


    //Output amount they have to pay (HALF)
    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}




// TODO: Complete the function (Bill amount + sales percent of bill + tip percent of bill / 2)
float half(float bill, float tax, int tip)
{

    float total = bill + (tax / 100) * bill;
    float half_amount = (total / 2);
    float individual = (half_amount * ((float) tip / 100)) + half_amount;



    return individual;
}
