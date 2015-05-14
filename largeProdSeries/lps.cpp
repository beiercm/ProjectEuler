#include <iostream>

int main()
{
	
	int i, j, lines = 20, maxSize = 1000, target = 13;
	std::string block[lines];
	std::string totalString;
	int *numArray = new int[maxSize];
	long long int max, prod;

	for(i = 0; i < lines; i++)
	{
		std::cin>>block[i];
		totalString = totalString + block[i];
	}

	for(i = 0; i < maxSize; i++)
		numArray[i] = totalString[i] - '0';

	for(i = 0; i < maxSize - target; i++)
	{
		prod = 1;

		for(j = i; j < i + target; j++)
			prod *= numArray[j];

		std::cout<<"Product = "<<prod<<"\n";

		if(prod > max)
			max = prod;
	}

	std::cout<<max<<"\n";
}