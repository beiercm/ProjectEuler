def factDigSum(n):
	fact = 1
	for i in range(1, n + 1):
		fact *= i

	return fact

def sepNum(n):
	numSum = 0
	m = 10
	while n > 0:
		numSum += (n % m)
		n //= m

	return numSum

def main():
	n = 100

	print(sepNum(factDigSum(n)))

main()