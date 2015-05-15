def findEvenFibSum(upperLimit):
	evenSum = 0

	f1 = 1
	f2 = 1
	f3 = 0

	while f3 < upperLimit:
		f3 = f1 + f2
		f1 = f2
		f2 = f3

		if f3 % 2 == 0:
			evenSum += f3

	return evenSum

def main():
	print(findEvenFibSum(4000000))

main()