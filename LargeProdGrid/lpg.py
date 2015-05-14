def readData(fileName):
	inputFile = open(fileName)
	grid = []
	for line in inputFile:
		line = line.strip().split(' ')
		grid.append([int(x) for x in line])

	return grid

def findMaxProd(grid):
	for i in range(len(grid) )

def main():

	grid = readData("lpg.in")

	print(grid)

main()