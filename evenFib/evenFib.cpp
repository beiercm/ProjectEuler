#include <iostream>

int main()
{
	int f1 = 0, f2 = 1, f3, sum = 0, target = 4000000;

	while(true)
	{
		f3 = f2 + f1;

		if(f3 > target)
			break;

		if(f3 % 2 == 0)
			sum += f3;

		f1 = f2;
		f2 = f3;
	}

	std::cout<< sum << "\n";
}