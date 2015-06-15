def readData():
	numList = []
	inputFile = open("LargestProd.in")

	for line in inputFile:
		line = line.strip()
		line = reverseString(line)
		subList = genListFromInt(int(line))
		numList = addSubList(numList, subList)

	return numList

def genListFromInt(n):
	subList = []
	div = 10
	numCount = 50

	while(numCount > 0):
		subList.append(n % div)
		n //= div
		numCount -= 1

	return subList

def addSubList(numList, subList):
	for n in subList:
		numList.append(n)

	return numList

def reverseString(someString):
	someString = someString[::-1]

	return someString

def findLargestProd(numList, n):
	maxProd = 0
	prod = 1

	for i in range(0, len(numList) - n):

		prod = numList[i]

		for j in range(i + 1, i + n):
			prod = prod * numList[j]

		maxProd = max(maxProd, prod)

	return maxProd


def main():
	numList = readData()
	print(findLargestProd(numList, 13))

main()