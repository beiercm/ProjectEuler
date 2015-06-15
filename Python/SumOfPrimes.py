def sumPrimes(n):
	sieveList = [x for x in range(n + 1)]

	sieveList[1] = 0

	primeSum = 0

	for i in range(len(sieveList)):
		if sieveList[i] != 0:
			mult = 1
			prod = 1
			primeSum += sieveList[i]

			while prod <= n:
				sieveList[prod] = 0
				mult += 1
				prod = sieveList[i] * mult

	return primeSum

def main():
	print(sumPrimes(2000000))

main()