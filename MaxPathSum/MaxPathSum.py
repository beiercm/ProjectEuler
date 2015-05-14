def readData(fileName):
	inputFile = open(fileName)
	inputList = []

	for line in inputFile:
		line = line.strip().split(' ')
		inputList.append([int(x) for x in line])
	return inputList

def findMaxPath(treeList):
	for i in range(len(treeList) - 2, -1, -1):
		for j in range(len(treeList[i])):
			leftSum = treeList[i][j] + treeList[i+1][j]
			rightSum = treeList[i][j] + treeList[i+1][j+1]
			treeList[i][j] = max(leftSum, rightSum)

	return treeList[0][0]


#Works but terrible implementation, horrible runtime
def findMaxPath2(treeList):
	return findMaxPathHelper(treeList, 0, 0, len(treeList))

def findMaxPathHelper(treeList, depth, index, maxDepth):
	if depth == maxDepth - 1:
		print(treeList[depth][index])
		return treeList[depth][index]

	leftSum = treeList[depth][index] + findMaxPathHelper(treeList, depth + 1, index, maxDepth)
	rightSum = treeList[depth][index] + findMaxPathHelper(treeList, depth + 1, index + 1, maxDepth)

	return max(leftSum, rightSum)

def main():
	print(findMaxPath(readData("tree1.in")))
	print(findMaxPath(readData("tree2.in")))
	print(findMaxPath(readData("tree3.in")))
main()