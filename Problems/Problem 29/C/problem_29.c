#include <time.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * Problem 29 from Project Euler
 *
 * Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:
 *
 * 2^2=4, 2^3=8, 2^4=16, 2^5=32
 * 3^2=9, 3^3=27, 3^4=81, 3^5=243
 * 4^2=16, 4^3=64, 4^4=256, 4^5=1024
 * 5^2=25, 5^3=125, 5^4=625, 5^5=3125
 * If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:
 *
 * 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
 *
 * How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
 *
 * PLEASE NOTE
 * In order to compile you must have gcc, or similar, installed
 *
 * REGARDING THE PERFORMANCE
 * This is not the final Algorithm, anyone can improve it.
 * If you have a better solution please submit a pull request, or an issue, on Github
 *
 * @author Claudio Ludovico Panetta (@Ludo237)
 *
 * @version 1.0.0
 **/
#define MAX 100 // Maximum sequence
#define VALUES (int)(log(MAX)/log(2)) // Maximum values
/**
 * To be honest this is not a real algorithm
 * I'm using unix to pass some arguments to this file
 * because this is a real simple "Pencil and Paper" problems
 * and I found it difficult to translate in some sort of complete
 * Algorithm, and keep it fast."
 * @param sort -n "Sort lines on a text file but compare according to string numerical value"
 * @param uniq "Report or omit repeated lines"
 * @praram wc -l "Print newline, word, and byte counts for each line"
 **/
int main(int argc, char *argv[])
{
    // Benchmark variable
    double start, end;
    // Algorithm starts
    printf("Params received.\n");
    printf("Alrogithm starts, please wait...\n");
    start = clock();
    for(unsigned int i = 2; i <= MAX; i++)
    {
        for(unsigned int j = 2; j <= MAX; j++)
        {
            printf("%0.10f\n", log(i) * j); // This is where the algorithm can prints the result;
        }
    }
    end = clock();
    printf("Algorithm end.\n");
    printf("Total time: %f\n", (end - start)/CLOCKS_PER_SEC);
    return 0;
}
