def findLargestPrimeFactor(n):
	div = 2

	#gets the even factors out of the way
	while n % div == 0:
		n /= div

	div = 3

	while n > div:
		if n % div == 0:
			n /= div
		else:
			div += 2

	return div

#testing git pull
def main():
	print(findLargestPrimeFactor(600851475143))

main()
