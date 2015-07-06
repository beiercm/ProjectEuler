def sumTarg(a, b, c, n):
	return (a + b + c == n)

def perfSq(a, b, c):
	return ((a * a) + (b * b) == (c * c))
		
def pythagTrip(n):

	for c in range(2, n - 2):
		for b in range(1, c):
			a = n - (c + b)
			if sumTarg(a, b, c, n) and perfSq(a, b, c):
				print(a, b, c)
				return a * b * c

	return -1

def main():
	print(pythagTrip(1000))



main()