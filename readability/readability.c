#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int coleman_liau(int letters, int words, int sentences);

int main(void)
{
    //TODO: Get string
    string text = get_string("Text: ");

    //TODO: count letters, words and sentences
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    //TODO: Coleman-liau count
    int col = coleman_liau(letters, words, sentences);

    //TODO: printf time
    if (col < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (col >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", col);
    }

}


int count_letters(string text)
{
    //TODO: Count numbers of letters
    int count = 0;
    for (int i = 0, len = strlen(text);  i < len; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

int count_words(string text)
{
    //TODO: Count numbers of words
    int count = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == ' ')
        {
            count++;
        }
    }
    return count + 1;
}

int count_sentences(string text)
{
    //TODO: Count numbers of sentences
    int count = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}

int coleman_liau(int letters, int words, int sentences)
{
    //TODO: Count Coleman-liau
    float letter = (float) letters / words * 100;
    float sentence = (float) sentences / words * 100;

    int col = round(0.0588 * letter - 0.296 * sentence - 15.8);
    return col;

}