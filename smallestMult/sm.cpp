#include <iostream>

int main()
{
	int cases, i, c, num, start;

	std::cin>>cases;

	for(c = 0; c < cases; c++)
	{
		std::cin>>start;
		num = start;

		while(true)
		{
			for(i = start; i > 1; i--)
				if(num % i != 0)
					break;
	
			if(i == 1)
				break;
			else
				num += start;
		}
		
		std::cout<<num<<"\n";
	}
}