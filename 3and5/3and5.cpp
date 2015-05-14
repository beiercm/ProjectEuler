#include <iostream>

int main()
{
	int n = 0, sum = 0;

	while(n < 1000)
	{
		if(n % 3 == 0 || n % 5 == 0)
			sum += n;

		n++;
	}

	std::cout<< sum <<"\n";
}