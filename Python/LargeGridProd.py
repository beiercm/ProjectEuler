def readData(filename):
	inputFile = open(filename)

	grid = []

	for line in inputFile:
		line = line.strip().split(' ')
		line = [int(x) for x in line]
		grid.append(line)

	return grid

#Does the same thing as the above function, one line for shits and giggles
def readData2(filename):
	return [[int(x) for x in line.strip().split(' ')] for line in open(filename)]

def findMaxProd(grid, n):
	maxHorizProd, maxVertProd, maxDownAndRightDiag, maxUpAndRightDiag = 0, 0, 0, 0
	length = len(grid)

	for row in range(0, length):
		for i in range(0, length):
			vertProd = grid[row][i]
			horizProd = grid[row][i]
			downandRightDiag = grid[row][i]
			upAndRightDiag = grid[row][i]

			for j in range(1, n):
				vertProd *= grid[(row + j) % length][i]
				horizProd *= grid[row][(i + j) % length]
				downandRightDiag *= grid[(row + j) % length][(i + j) % length]
				upAndRightDiag *= grid[(row - j)][(i + j) % length]

			maxHorizProd = max(maxHorizProd, horizProd)
			maxVertProd = max(maxVertProd, vertProd)
			maxDownAndRightDiag = max(maxDownAndRightDiag, downandRightDiag)
			maxUpAndRightDiag = max(maxUpAndRightDiag, upAndRightDiag)

	return max(maxHorizProd, maxVertProd, maxDownAndRightDiag, maxUpAndRightDiag)


def findLargestProd(filename, n):
	grid = readData2(filename)
	return findMaxProd(grid, n)

def main():
	print(findLargestProd("LargeGridProd.in", 4))

main()