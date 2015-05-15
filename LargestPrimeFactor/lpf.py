def findLargestPrimeFactor(n):
	div = 2

	while n > div:
		if n % div == 0:
			n /= div
		else:
			div += 1

		print(n)

	return div

def main():
	print(findLargestPrimeFactor(600851475143))

main()