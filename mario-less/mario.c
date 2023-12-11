#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    // TODO: Prompt for input Height
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // TODO: Prompt for building using ('#')
    for (int h = 0; h < height; h++)
    {
        for (int c = 0; c < height; c++)
        {
            // TODO: Prompt right
            if (c < height - h - 1)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }

}
