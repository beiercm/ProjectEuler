import time

def sq(n):
	return n**2

def sqrt(n):
	return n**(1/2)

def findHypot(a, b):
	return a + b + sqrt(sq(a) + sq(b))

def printSides(a, b, rtSum):
	print("{", a, ",", b, ",", rtSum, "}")	

#First implementation, horrible runtime, at least O(n^3) with the other function
def findNumSol2(n):
	numSol = 0

	for a in range(1, n - 2):
		for b in range(a+1, n - 1):
			rtSum = findHypot(a, b)

			if rtSum == n:
				#printSides(a, b, int(rtSum))
				numSol += 1


	return numSol

#After looking at the numbers, realized that 'a' must be a factor of 'n'
#Runs in a few seconds compared to the original not even finishing
def findNumSol(n):
	numSol = 0

	for a in range(2, int(n/3)):
		if(n % a == 0):
			for b in range(a + 1, n - a):

				rtSum = findHypot(a, b)

				if rtSum == n:
					#printSides(a, b, int(rtSum))
					numSol += 1

	return numSol

def maxNumSol(n):

	maxSol = 0
	numSol = 0
	maxInt = 0

	for i in range(2, n):
		numSol = findNumSol(i)

		if numSol > maxSol:
			maxSol = numSol
			maxInt = i
			print(maxSol, " ", i)

	return maxInt

def main():
	initTime = time.clock()
	print(maxNumSol(1000))

	print(time.clock() - initTime)
main()