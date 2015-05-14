def sepNum(n):
	digitList = []
	m = 10
	while n > 0:
		digitList.append(n % m)
		n //= m
		m * 10

	return digitList

def calcPowers(digitList, power):
	numSum = 0
	for n in digitList:
		numSum += n ** power
		
	return numSum


def digitPowers(power, limit):
	numList = []
	for i in range(2, limit):
		if i == calcPowers(sepNum(i), power):
			numList.append(i)
			print(i)

	return numList

def main():
	power = 5
	limit = 1000000

	numList = digitPowers(power, limit)
	print(numList)
	print(sum(numList))

main()