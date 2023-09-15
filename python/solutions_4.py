def is_palindrome(n):
	s = str(n)
	mid = round(len(s) / 2)
	first_half = s[:mid]

	if len(s) % 2 == 0:		
		second_half = s[mid:]
	else:
		second_half = s[mid + 1:]

	
	return first_half == second_half[::-1]

def naive_solution():
	n1 = 999
	n2 = 999
	max_palindrome = 0

	while n1 > 1:
		n2 = n1

		while n2 > 1:
			num = n1 * n2
			if is_palindrome(num):
				max_palindrome = max(max_palindrome, num)
			n2 -= 1

		n1 -= 1

	print(max_palindrome)

def new_solution():
	n = 999
	max_num = n ** 2

	while max_num > 10:
		if is_palindrome(max_num):
			n1 = n
			while n1 > 1:
				n2 = max_num / n1

				if n2 > n1:
					n1 -= 1
					continue
				if n2 % 1 == 0:
					print(max_num, n1, n2)
					return
				n1 -= 1
		max_num -= 1

import time

start_time = time.time()
naive_solution()
print(time.time() - start_time)

start_time = time.time()
new_solution()
print(time.time() - start_time)