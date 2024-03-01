// Maimoona Aziz
#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
int decimal_value(string text, int length, int dec_val[]);
int binary_value(int dec_val[], int length, int bi_val[length][BITS_IN_BYTE]);

int main(void)
{
    // Ask for text
    string text = get_string("Message: ");

    const int length = strlen(text); // Variable for length of inputted text
    int dec_val[length];             // Array variable for storing the decimal value of each character of inputted text
    int bit[length][BITS_IN_BYTE];   // Array variable for storing the binary value of each character of inputted text

    // Functions doing their jobs
    decimal_value(text, length, dec_val);
    binary_value(dec_val, length, bit);

    // Printing bulbs
    for (int l = 0; l < length; l++) // Loop for each letter
    {
        for (int m = BITS_IN_BYTE - 1; m >= 0; m--) // Loop for printing each bulb for each letter
        {
            print_bulb(bit[l][m]); // Prints bulb
        }
        printf("\n"); // Next line when each letter is done
    }
}

// Function that converts inputted text to decimal (input word and output decimal)
int decimal_value(string text, int length, int dec_val[])
{
    // Loops through each character in the text
    for (int i = 0; i < length; i++)
    {
        // Converts text to its decimal ASCII value
        dec_val[i] = (int) text[i];
    }
    return dec_val[length - 1]; // Stores it in 'dec_val' array variable
}

// Function that converts decimals to binary (input decimal and output binary)
int binary_value(int dec_val[], int length, int bit[length][BITS_IN_BYTE])
{
    // Loops through each character in the text
    for (int j = 0; j < length; j++)
    {
        // Variable that holds current decimal value of character being converted to binary.
        int c_val = dec_val[j];

        // Loops through each character in current word until it reaches 8 bits
        for (int k = 0; k < BITS_IN_BYTE; k++)
        {
            bit[j][k] = c_val % 2; // Divides by 2
            c_val = c_val / 2;     // Calculates the remainder of of current value by 2 until it reaches '0' or '1'
        }
    }
    return bit[length - 1][BITS_IN_BYTE - 1]; // Stores it in 'bit' array variable
}

// Function prints on or off bulbs
void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}