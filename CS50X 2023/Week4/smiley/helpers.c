// Maimoona Aziz
#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int i = 0; i < height; i++) // Every vertical black pixel
    {
        for (int j = 0; j < width; j++) // Every horizontal black pixel
        {
            // If I find a black pixel (when all 0x00)
            if (image[i][j].rgbtRed == 0x00 && image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtBlue == 0x00)
            {
                // Color it an ashy blue
                image[i][j].rgbtRed = 0x3A;
                image[i][j].rgbtGreen = 0x5E;
                image[i][j].rgbtBlue = 0x8B;
            }
        }
    }
}
