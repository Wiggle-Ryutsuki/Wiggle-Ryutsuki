// Maimoona Aziz
// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

int word_count = 0;

// TODO: Choose number of buckets in hash table
const unsigned int N = 27;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Hash the word to get the index in the hash table
    unsigned int index = hash(word);

    // Traverse the linked list at the index in the hash table to see if the word is there
    // Cursor = table[index], if cursor is not NULL, go next
    for (node *cursor = table[index]; cursor != NULL; cursor = cursor->next)
    {
        if (strcasecmp(cursor->word, word) == 0) // Comparing
        {
            return true; // Hash found, return true
        }
    }

    return false; // Hash not found, return false
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function

    // Set Hash value to 0
    unsigned int hash_val = 0;
    // Random prime number for uniqueness
    unsigned int prime = 107;

    // For each character
    for (int i = 0, l = strlen(word); i < l; i++)
    {
        int char_val = ((toupper(word[i]) - 'A') + 1);

        if (word[i] == '\'')
        {
            char_val = 27; // Value for apostophe (27 because the alphabet is 26)
        }

        // Multiply letter by its position (so that it is unique, like values for "eat" and "tea")
        int multi = 0;
        multi = char_val * i;

        // Calculating hash, multiply hash with prime and multiple of its position
        hash_val = hash_val * prime + multi;
    }
    return hash_val % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO:

    // Open dictionary
    FILE *infile = fopen(dictionary, "r");
    if (infile == NULL)
    {
        printf("Unable to open file\n");
        return false;
    }

    // Buffer to read words into
    char word[LENGTH];

    // Read strings from file one at a time
    while (fscanf(infile, "%s", word) == 1)
    {
        // Create new node for each word
        node *new = malloc(sizeof(node)); // Allocate memory
        if (new == NULL)                  // Check if NULL
        {
            printf("Unable to allocate memory\n");
            fclose(infile);
            return false;
        }

        // Copy word into node
        strcpy(new->word, word);
        int index = hash(word);
        new->next = table[index];
        table[index] = new;

        // Counts number of words
        word_count++;
    }

    fclose(infile);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    // word_count has been declared as a global variable
    // In load, after successfully copying words into node, it adds 1 to word_count
    return word_count; // Just return word_count
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // For every bucket in the table
    for (int i = 0; i < N; i++)
    {
        // Set cursor to point at current node
        node *cursor = table[i];
        // While current is not NULL
        while (cursor != NULL)
        {
            node *temp = cursor;   // Temporary cursor to current cursor
            cursor = cursor->next; // Current cursor = next node
            free(temp);            // Free temporary
        }
    }
    return true;
}
