def fib(digitSize):
	n1 = 1
	n2 = 1
	n3 = 1
	term = 2

	digitSize = 10 ** (digitSize - 1)

	if digitSize < 3:
		return n1

	while n3 // digitSize == 0:
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		term += 1

	return term

def main():
	print(fib(1000))

main()