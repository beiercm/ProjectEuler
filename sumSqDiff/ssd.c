/*
	Project Euler - 6 - Sum square difference
*/

#include <stdio.h>

int myPow(int x, int n)
{
	if(n < 1)
		return 1;

	return x * myPow(x, n - 1);
}

int main()
{
	int i, sum1 = 0, sum2 = 0, upperBound = 100;

	for(i = 1; i <= upperBound; i++)
	{
		sum1 += myPow(i, 2);
	}

	sum2 = upperBound * (upperBound + 1) / 2.0;

	sum2 = myPow(sum2, 2);

	printf("%d\n", sum2 - sum1);

	return 0;
}