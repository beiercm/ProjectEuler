/*
	ProjectEuler - 3 - Largest Primer Factor
	6/15/16
*/

#include <stdio.h>

int main()
{
	long long int num = 600851475143;
	int maxPrime = 0, divider = 2;

	while(num > 1)
	{
		if(num % divider == 0)
		{
			num /= divider;

			if(divider > maxPrime)
				maxPrime = divider;
		}
		else
			divider++;
	}

	printf("%d\n", maxPrime);

	return 0;
}