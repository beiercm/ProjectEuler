def fact(n):
	if n < 2:
		return 1

	return n * fact(n - 1)

def sepNum(n):
	digitList = []
	m = 10

	while n > 0:
		digitList.append(n % m)
		n = n // m

	return digitList

def digitFactorials(limit):
	factSum = 0

	for i in range(3, limit):
		if i == sum(list(map(fact, sepNum(i)))):
			factSum += i
			print(i)

	return factSum

def main():
	print(digitFactorials(1000000))

	#print(sum(list(map(fact, sepNum(145)))))

main()
