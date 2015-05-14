/*
	Project Euler - 7 - 10001st prime
*/

#include <stdio.h>

int main()
{
	int target = 100001;
	int prime[target];
	int i, count = 1, num = 3;
	int stop = 1;

	for(i = 0; i < target; i++)
		prime[i] = 0;

	
	prime[0] = 2;


	while(stop == 1)
	{
		for(i = 0; i < target && prime[i] != 0; i++)
			if(num % prime[i] == 0)
			{
				num += 2;
				break;
			}
			else if(i == count - 1)
			{
				prime[i + 1] = num;
				num += 2;
				count++;
				break;
			}
			else if(count == target)
				stop = 0;

	}

	printf("%d\n", prime[target - 1]);

	return 0;

}