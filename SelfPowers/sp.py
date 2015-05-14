def sumSelfPower(upperlimit):
	powSum = 0

	for i in range(1, upperlimit + 1):
		powSum += i**i

	return powSum;

def main():
	upperLimit = 1000
	numDigits = 10
	print(sumSelfPower(upperLimit) % (10 ** numDigits))

main()
