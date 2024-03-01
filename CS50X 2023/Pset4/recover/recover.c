// Maimoona Aziz
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;
int BLOCKSIZE = 512;

int main(int argc, char *argv[])
{
    // Check for command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Make it easier to remember input file name
    char *infile = argv[1];

    // Open input file
    FILE *file = fopen(infile, "r");
    if (file == NULL) // Check if you can open file
    {
        printf("Unable to open file\n");
        return 1;
    }

    BYTE buffer[BLOCKSIZE];
    bool found = false; // Variable that detects if JPEG header is found
    FILE *img = NULL;
    int file_no = 0;       // File number
    int current_file = -1; // Current file number

    // Read file
    while (fread(buffer, 1, BLOCKSIZE, file) == BLOCKSIZE)
    {
        // Check for  JPEG header
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close any "previous" JPEG files
            if (img != NULL)
            {
                fclose(img);
            }

            // Allocate memory
            char jfile[8];

            // Name the file
            sprintf(jfile, "%03i.jpg", file_no);

            // Open new JPEG file for writing
            img = fopen(jfile, "w");
            if (img == NULL) // Check if able to open
            {
                printf("Unable to open file\n");
                fclose(file);
                return 3;
            }

            // If found, true
            found = true;
            file_no++;
        }

        // If found, write file
        if (found == true && img != NULL)
        {
            fwrite(buffer, 1, BLOCKSIZE, img);
        }
    }

    // Close files
    if (img != NULL)
    {
        fclose(img);
    }

    fclose(file);

    return 0;
}