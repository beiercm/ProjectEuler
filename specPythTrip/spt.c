/*
	Project Euler - 9 - Special Pythagorean triplet
	6/15/14
*/

#include <stdio.h>

int main()
{
	int a, b, c, target = 1000;

	for(a = 1; a <= target - 2; a++)
		for(b = 1; b <= target - 2; b++)
			for(c = 1; c <= target - 2; c++)
				if(a + b + c == target)
					if((a * a) + (b * b) == (c * c))
					{
						printf("%d\n", a * b * c);
						return 0;
					}

	return 0;
}