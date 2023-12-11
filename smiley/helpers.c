#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    // This is a nested loop that loops through each pixel in the image. The outer loop (i) iterates through the columns (width) of the image, while the inner loop (l) iterates through the rows (height) of the image.
    for (int i = 0; i < width; i++)
    {
        for (int l = 0; l < height; l++)
        {
            // This if checks if the current pixel is black, that is, if the red, green and blue components (rgbtRed, rgbtGreen and rgbtBlue, respectively) are all equal to zero. If applicable, components are changed to a specific value.
            if (image[l][i].rgbtBlue == 0 && image[l][i].rgbtGreen == 0 && image[l][i].rgbtRed == 0)
            {
                image[l][i].rgbtBlue = 99;
                image[l][i].rgbtGreen = 23;
                image[l][i].rgbtRed = 164;
            }
        }
    }
}

