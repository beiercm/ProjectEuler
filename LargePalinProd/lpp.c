/*
	ProjectEuler - 4 - LargestPalidrome Product
	6/15/14
*/

#include <stdio.h>

int isPalin(int num)
{
	int numArray[6];
	int size = 0, num2 = num, rem, i;
	int hi, lo = 0;

	if(num < 10)
		return 0;

	while(num2 > 0)
	{
		rem = num2 % 10;
		num2 /= 10;
		numArray[size] = rem;
		size++;
	}

	hi = size - 1;

	while(hi >= lo)
	{
		if(numArray[hi] != numArray[lo])
			return 0;
		lo++;
		hi--;
	}

	return 1;
}

int main()
{
	int i, j, upperBound = 1000;
	int maxPalin = 0;

	for(i = 0; i < upperBound; i++)
		for(j = 0; j < upperBound; j++)
			if(isPalin(i * j))
			{
				if(i * j > maxPalin)
					maxPalin = i * j;
			}

	printf("%d\n", maxPalin);

	return 0;
}