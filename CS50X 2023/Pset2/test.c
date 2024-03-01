#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

int decimal_value(string text, int length, int dec_val[]);
int binary_value(int dec_val[], int length, int bi_val[length][BITS_IN_BYTE]);

int main(void)
{
    // Ask for text
    string text = get_string("Message: ");

    int length = strlen(text);
    int dec_val[length];
    int bi_val[length][BITS_IN_BYTE];

    decimal_value(text, length, dec_val);
    binary_value(dec_val, length, bi_val);

    // Printing decimals
    for (int i = 0; i < length; i++)
    {
        printf("%i ", dec_val[i]);
    }
    printf("\n");

    // Printing binary
    for (int i = 0; i < length; i++)
    {
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            printf("%i", bi_val[i][j]);
        }
        printf(" ");
    }
    printf("\n");
}

// Function that converts words to decimal
int decimal_value(string text, int length, int dec_val[])
{
    for (int i = 0; i < length; i++)
    {
        dec_val[i] = (int) text[i];
    }
    return dec_val[length - 1];
}

// Function that converts decimals to binary
int binary_value(int dec_val[], int length, int bi_val[length][BITS_IN_BYTE])
{
    for (int j = 0; j < length; j++)
    {
        int c_val = dec_val[j];
        for (int k = BITS_IN_BYTE - 1; k >= 0; k--)
        {
            bi_val[j][k] = c_val % 2;
            c_val = c_val / 2;
        }
    }
    return bi_val[length - 1][BITS_IN_BYTE - 1];
}