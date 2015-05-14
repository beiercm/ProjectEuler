import time

def makePent(n):
	return int((n * (3 * n - 1) / 2))

def makePentList(n):
	return [makePent(x) for x in range(1, n)]


def binSearch(n, pentList):
	return binSearchHelper(n, pentList, 0, len(pentList) - 1)

def binSearchHelper(n, pentList, imin, imax):

	while imax >= imin:
		imid = (imax + imin) // 2

		if pentList[imid] > n:
			imax = imid - 1
		elif pentList[imid] < n:
			imin = imid + 1
		else:
			return True

	return False

def findPentSumEqualDiff(n):
	pentList = makePentList(n)

	t0 = time.clock()

	for i in range(len(pentList) - 1):
		for j in range(i + 1, len(pentList)):
			a = pentList[i]
			b = pentList[j]

			if binSearch((a + b), pentList) and binSearch((b - a), pentList):
			#if (b-a) in pentList and (a + b) in pentList:
				print(time.clock() - t0)
				return (b - a)

	print(time.clock() - t0)
	return "Not found"
def main():
	print(findPentSumEqualDiff(10000))

main()