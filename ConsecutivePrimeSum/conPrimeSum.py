def genPrimeSieve(upperLimit):
	primeList = [1 for x in range(upperLimit)]
	primeList[0] = 0
	primeList[1] = 0

	n = 2

	while n < (upperLimit ** .5):
		p = 2
		prod = 1

		while prod < upperLimit:
			prod = p * n
		
			if prod >= upperLimit:
				break

			primeList[prod] = 0

			p += 1

		n += 1

	return primeList

def prettifyPrimeList(primeList):
	prettyPrimeList = []

	for i in range(len(primeList)):
		if primeList[i] == 1:
			prettyPrimeList.append(i)

	return prettyPrimeList

#most likely a horrible implementation
# < 100,000 runs instantly
# 100,000 takes a few seconds, 
# 1,000,000 takes a long while.  
def findLargestPrimeSum(upperLimit):
	primeList = prettifyPrimeList(genPrimeSieve(upperLimit))

	maxRange = 0
	maxPrime = 0

	for i in range(len(primeList)):
		testSum = 0
		size = 3
		prevTestSum = 1

		while testSum < upperLimit - 5 and testSum != prevTestSum:

			if testSum % 2 != 0 and testSum in primeList:
				if size > maxRange:
					maxRange = size - 1
					maxPrime = testSum
					print(testSum)
					
			prevTestSum = testSum
			testSum = sum(primeList[i : i + size])					

			size += 1
		
	print(maxRange, maxPrime)


def main():
	print(findLargestPrimeSum(100000))

main()