/*
	Project Euler - 5 - Smallest Multiple
*/

#include <stdio.h>

int main()
{
	int n = 1, j, upperBound = 20;

	while(1)
	{
		for(j = 1; j <= upperBound; j++)
			if(n % j != 0)
				break;

		if(j == upperBound + 1)
		{
			printf("%d\n", n);
			break;
		}

		n++;
	}
}