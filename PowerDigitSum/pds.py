def sepNum(n):
	numSum = 0
	m = 10
	while n > 0:
		numSum += (n % m)
		n //= m

	return numSum

def main():
	print(sepNum(2 ** 1000))

main()