// Maimoona Aziz
#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through height
    for (int i = 0; i < height; i++)
    {
        // Loop through width
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            // Calculate average values
            int avg = round((red + green + blue) / 3.0);

            // Change values
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through height
    for (int i = 0; i < height; i++)
    {
        // Loop through width
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            // Calculate sepia formula
            int s_red = round(0.393 * red + 0.769 * green + 0.189 * blue);
            int s_green = round(0.349 * red + 0.686 * green + 0.168 * blue);
            int s_blue = round(0.272 * red + 0.534 * green + 0.131 * blue);

            // Check if result values are within 0 - 255
            if (s_red > 255)
            {
                s_red = 255;
            }
            else if (s_red < 0)
            {
                s_red = 0;
            }

            if (s_green > 255)
            {
                s_green = 255;
            }
            else if (s_green < 0)
            {
                s_green = 0;
            }

            if (s_blue > 255)
            {
                s_blue = 255;
            }
            else if (s_blue < 0)
            {
                s_blue = 0;
            }

            // Change values
            image[i][j].rgbtRed = s_red;
            image[i][j].rgbtGreen = s_green;
            image[i][j].rgbtBlue = s_blue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        // Loop half of width (because we're switching the start and end pieces and it will likely end in the middle)
        for (int j = 0; j < width / 2; j++)
        {
            // Flipping rows
            RGBTRIPLE temp = image[i][j];          // Temporary variable holds start
            image[i][j] = image[i][width - 1 - j]; // The end pixel occupies start space
            image[i][width - 1 - j] = temp;        // Temporary varible (start pixel) now occupies end space
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    {
        RGBTRIPLE copy[height][width];

        // Creating copy of the original image
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                copy[i][j] = image[i][j];
            }
        }

        // Loop that blurs image
        // Loop through height
        for (int i = 0; i < height; i++)
        {
            // Loop through width
            for (int j = 0; j < width; j++)
            {
                int red = 0, green = 0, blue = 0;
                float counter = 0;

                // Horizontal pixels
                for (int row = i - 1; row <= i + 1; row++)
                {
                    // Vertical pixels
                    for (int col = j - 1; col <= j + 1; col++)
                    {
                        // Check if within image range
                        if (row >= 0 && row < height && col >= 0 && col < width)
                        {
                            // Add up sum
                            red += copy[row][col].rgbtRed;
                            green += copy[row][col].rgbtGreen;
                            blue += copy[row][col].rgbtBlue;
                            counter++;
                        }
                    }
                }

                // Calculate average then change values of OG image
                image[i][j].rgbtRed = round(red / counter);
                image[i][j].rgbtGreen = round(green / counter);
                image[i][j].rgbtBlue = round(blue / counter);
            }
        }

        return;
    }
}
