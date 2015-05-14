/*
	Project Euler - 2 - Even Fib sum
	6/15/16
*/

#include <stdio.h>

int main()
{
	int sum = 0;
	int i, upperBound = 4000000;
	int f1 = 0, f2 = 1, f3 = 0;

	while(f3 < upperBound)
	{
		f3 = f2 + f1;

		if(f3 % 2 == 0)
			sum += f3;

		f1 = f2;
		f2 = f3;
	}

	printf("%d\n", sum);

	return 0;
}	