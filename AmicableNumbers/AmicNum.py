def sumOfDivisors(n):
	divSum = 1
	div = 2

	while div <= (n / 2):
		if n % div == 0:
			divSum += div

		div += 1
	return divSum

def getAmicableNum(limit):
	amicNumList = []

	for i in range(limit):
		divSum = sumOfDivisors(i)

		if i == sumOfDivisors(divSum) and i != divSum and i not in amicNumList:
			print(i, divSum)
			amicNumList.append(i)

	print(amicNumList)
	return amicNumList

def main():


	print(sum(getAmicableNum(10000)))

main()
