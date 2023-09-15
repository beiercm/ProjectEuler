fib = [1, 2]
max_num = 4000000
_sum = 2

current_pos = 2

while fib[-1] <= max_num:
	num1 = fib[current_pos - 2]
	num2 = fib[current_pos - 1]
	new_fib = num1 + num2

	if new_fib > max_num:
		break

	if new_fib % 2 == 0:
		_sum += new_fib

		print(new_fib, _sum)

	fib.append(num1 + num2)

	current_pos += 1

print(_sum)