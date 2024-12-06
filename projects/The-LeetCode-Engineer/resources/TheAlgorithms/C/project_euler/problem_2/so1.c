/**
 * \file
 * \brief [Problem 2](https://projecteuler.net/problem=2) solution
 *
 * Problem:
 *
 * Each new term in the Fibonacci sequence is generated by adding the previous
 * two terms. By starting with 1 and 2, the first 10 terms will be:
 * `1,2,3,5,8,13,21,34,55,89,..`
 * By considering the terms in the Fibonacci sequence whose values do not exceed
 * n, find the sum of the even-valued terms. e.g. for n=10, we have {2,8}, sum
 * is 10.
 */
#include <stdio.h>

/** Main function */
int main()
{
    int n = 0;
    int sum = 0;
    int i = 1;
    int j = 2;
    int temp;
    scanf("%d", &n);

    while (j <= n)
    {
        if ((j & 1) == 0)  // can also use(j%2 == 0)
            sum += j;
        temp = i;
        i = j;
        j = temp + i;
    }

    printf("%d\n", sum);
    return 0;
}