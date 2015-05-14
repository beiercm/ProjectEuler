/*
	Project Euler - 8 - Largest Product in a series
	6/15/16
*/

#include <stdio.h>

int main()
{
	char string[20][51];
	int i, j, target = 13;
	int array[1000];
	unsigned long int prod, maxProd = 1;

	for(i = 0; i < 20; i++)
		scanf("%s", string[i]);

	for(i = 0; i < 20; i++)
		for(j = 0; j < 50; j++)
			array[(i * 50) + j] = string[i][j] - '0';



	for(i = 0; i < 1000 - target; i++)
	{
		prod = 1;
		for(j = i; j < i + target; j++)
		{
			prod *= array[j];

			if(prod > maxProd)
				maxProd = prod;
		}
	}

	printf("%lu\n", maxProd);


	return 0;


}