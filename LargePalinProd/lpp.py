def isPalindrome(p):
	p = str(p)
	i = 0
	j = len(p)

	while(True):
		if j <= 1 or j <= i:
			return True

		if p[i] != p[j - 1]:
			return False

		i += 1
		j -= 1

def findPalindrome(lowerLimit, upperLimit):
	maxPalin = 0

	for i in range(lowerLimit, upperLimit + 1):
		for j in range(i + 1, upperLimit + 1):
			prod = i * j
			if(isPalindrome(prod)):
				if maxPalin < prod:
					maxPalin = prod

	return maxPalin
			

def main():
	print(findPalindrome(100, 999))

main()