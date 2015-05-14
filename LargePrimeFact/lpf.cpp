#include <iostream>

int main()
{
	long int num;
	int i = 2, j, max;

	std::cin>>num;

	while(num > 1)
		(num % i == 0) ? num /= i : i++;
		
	std::cout<< "The largest prime factor is " << i << "\n";

}