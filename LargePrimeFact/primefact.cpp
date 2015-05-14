#include <iostream>

void zeroArray(int *array, int size)
{
	int i;

	for(i = 0; i < size; i++)
		array[i] = 0;
}

int main()
{
	int i, j, size = 10000, num;
	int array[size];

	for(i = 2; i < size; i++)
	{
		zeroArray(array, size);
		num = i;
		j = 2;

		while(num > 1)
		{
			if(num % j == 0)
			{
				num /= j;
				array[j]++;
			}
			else
				j++;
		}

		std::cout<<"Prime factorization of: "<<i<<"\n";

		for(j = 0; j < size; j++)
			if(array[j] > 0)				
				std::cout<< j <<"^"<<array[j]<<", ";

		std::cout<<"\n";
	}
}