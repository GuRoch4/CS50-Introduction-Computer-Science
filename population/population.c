#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start_size;
    int end_size;
    int years = 0;

    // TODO: Prompt for start size
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);

    // TODO: Prompt for end size
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size);

    // TODO: Calculate number of years until we reach threshold
    int population = start_size;
    while (population < end_size)
    {
        int born = population / 3;
        int dies = population / 4;
        population += born - dies;
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}
