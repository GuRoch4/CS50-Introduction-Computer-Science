#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //TODO: each row
    for (int i = 0; i < height; i++)
    {
        //TODO: each colum
        for (int j = 0; j < width; j++)
        {
            //TODO: pixel to float
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;

            //average value
            int average = round((red + green + blue) / 3);
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //TODO: each row
    for (int i = 0; i < height; i++)
    {
        //TODO: each colum
        for (int j = 0; j < width; j++)
        {
            //TODO: pixel to float
            float ored = image[i][j].rgbtRed;
            float ogreen = image[i][j].rgbtGreen;
            float oblue = image[i][j].rgbtBlue;

            //TODO: update pixel
            int sred = round(0.393 * ored + 0.769 * ogreen + 0.189 * oblue);
            int sgreen = round(0.349 * ored + 0.686 * ogreen + 0.168 * oblue);
            int sblue = round(0.272 * ored + 0.534 * ogreen + 0.131 * oblue);

            //TODO: if sepia "s" > 255 update pixel values
            if (sred > 255)
            {
                sred = 255;
            }
            if (sgreen > 255)
            {
                sgreen = 255;
            }
            if (sblue > 255)
            {
                sblue = 255;
            }

            //TODO: update pixel values
            image[i][j].rgbtRed = sred;
            image[i][j].rgbtGreen = sgreen;
            image[i][j].rgbtBlue = sblue;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //TODO: each row
    for (int i = 0; i < height; i++)
    {
        //TODO: each colum
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image [i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //TODO: copy image
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int tred, tgreen, tblue;
            tred = tgreen = tblue = 0;
            float counter = 0.00;
            //TODO: next pixel
            for (int m = -1; m < 2; m++)
            {
                for (int n = -1; n < 2; n++)
                {
                    int im = i + m;
                    int jn = j + n;
                    if (im < 0 || im > (height - 1) || jn < 0 || jn > (width - 1))
                    {
                        continue;
                    }

                    //TODO: image value
                    tred += image[im][jn].rgbtRed;
                    tgreen += image[im][jn].rgbtGreen;
                    tblue += image[im][jn].rgbtBlue;
                    counter++;


                }
                //TODO: averge next pixel
                temp[i][j].rgbtRed = round(tred / counter);
                temp[i][j].rgbtGreen = round(tgreen / counter);
                temp[i][j].rgbtBlue = round(tblue / counter);
            }
        }
    }
    //TODO: Original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;

        }
    }
    return;
}