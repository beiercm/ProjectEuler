def readData(fileName):
	inputFile = open(fileName)

	for line in inputFile:
		line = line.replace("\"", "").split(',')

	return sorted(line)

def scoreName(name):
	charSum = 0
	for char in name:
		charSum += ord(char) - ord('A') + 1

	return charSum

def sumList(nameList):
	totalSum = 0
	for i in range(0, len(nameList) + 1):
		score = scoreName(nameList[i - 1]) * i
		totalSum += score

	return totalSum


def main():
	nameList = readData("NamesScore.in")

	print(sumList(nameList))

	#print(nameList)

main()