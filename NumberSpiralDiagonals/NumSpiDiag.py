def spiral(n):
	spiralSum = 0
	offset = 2
	changeOffSet = 3
	limit = (n**2) + 1
	i = 1

	while i <= limit:
		spiralSum += i
		i += offset

		if i == changeOffSet ** 2:
			offset += 2
			changeOffSet += 2

	return spiralSum

def spiral2(n):
	spiralList = [x for x in range((n**2) + 1)]

	displacement = 2
	upperCorner = 3
	spiralSum = 0
	i = 1

	while i < len(spiralList):
		spiralSum += spiralList[i]
		i += displacement

		if i < len(spiralList) and spiralList[i] == (upperCorner ** 2):
			displacement += 2
			upperCorner += 2

	return spiralSum

def main():
	print(spiral(10001))

main()