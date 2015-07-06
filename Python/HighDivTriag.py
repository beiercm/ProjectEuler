def triangNum(n):
	return int(n * (n + 1)/2)

def numDiv(target):
	divTotal = 0
	n = 0

	while divTotal <= target:
		n += 1
		divTotal = findTotalDivs(triangNum(n))
		
	return triangNum(n)


def findTotalDivs(num):
	divProd = 1

	primeDict = numPrimesDiv(num)

	for key in primeDict:
		divProd *= primeDict[key] + 1

	return divProd

def numPrimesDiv(n):
	primeDict = {}
	div = 2

	while n > 1:
		while n % div == 0:
			if div in primeDict:
				primeDict[div] += 1
			else:
				primeDict[div] = 1

			n //= div

	return primeDict

def main():
	print(numDiv(500))

main()