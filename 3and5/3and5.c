/*
	Project Euler - 1 - Multiples of 3 and 5
	6/15/14

*/
#include <stdio.h>

int main()
{
	int i, upperBound = 1000, sum = 0;

	for(i = 0; i < upperBound; i++)
		if(i % 3 == 0 || i % 5 == 0)
			sum += i;

	printf("%d\n", sum);

	return 0;
}