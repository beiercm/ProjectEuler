#include <iostream>

void printArray(int *array, int size)
{
	int i;

	for(i = 0; i < size; i++)
		std::cout<<array[i]<<", ";

	std::cout<<"\n";
}

int main()
{
	int c, i, j, target, cases, count;
	int *primeArray;

	std::cin>>cases;

	for(c = 0; c < cases; c++)
	{
		std::cin>>target;
		primeArray = new int[target];
		primeArray[0] = 2;
		count = 1;
		j = 0;

		for(i = 3; count < target; i++)
		{
			j = 0;

			while(j < target && i % primeArray[j] != 0)
			{
				if(primeArray[j] * primeArray[j] > i)
				{
					primeArray[count] = i;
					count++;
					break;
				}

				j++;
			}
		}

		std::cout<<primeArray[target - 1]<<"\n";
		//printArray(primeArray, target);


	}
}