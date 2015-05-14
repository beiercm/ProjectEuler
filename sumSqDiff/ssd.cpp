#include <iostream>

int sumN(int n)
{
	return (n * (n + 1)) / 2;
}

int squareSum(int n)
{
	return sumN(n) * sumN(n);
}

int sumSquare(int n)
{
	int i, sum = 0;

	for(i = 1; i <= n; i++)
		sum += (i * i);

	return sum;
}

int main()
{
	int c, i, cases, sum, square, n;

	std::cin>>cases;

	for(c = 0; c < cases; c++)
	{
		std::cin>>n;

		std::cout<<squareSum(n) - sumSquare(n)<<"\n";
	}
}