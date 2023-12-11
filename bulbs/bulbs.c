#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO: Get string
    string message = get_string("Message: ");
    // TODO: message to binary
    for (int i = 0, len = strlen(message); i < len; i++)
    {
        // TODO: first step turning the text into decimal
        int decimal = (int) message[i];

        // TODO: second step turning the decimal into binary
        int bits[BITS_IN_BYTE];
        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
            bits[j] = decimal % 2;
            decimal /= 2;
        }

        //TODO: reverse order
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            print_bulb(bits[j]);
        }

        printf("\n");
    }
}

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
