def mult3And5(n, a, b):
	numSum = 0

	for i in range(n):
		if i % a == 0 or i % b == 0:
			numSum += i

	return numSum

def main():
	print(mult3And5(1000, 3, 5))

main()