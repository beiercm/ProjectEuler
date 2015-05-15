def sumOfSquares(n):
	sqSum = 0

	for i in range(n + 1):
		sqSum += (i * i)

	return sqSum

def squareOfSum(n):
	numSum = n * (n + 1) / 2

	return int(numSum * numSum)

def main():
	n = 100
	print(squareOfSum(n) - sumOfSquares(n))

main()