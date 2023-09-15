max_num = 1000
_sum = 0

for n in range(0, max_num):
	if n % 3 == 0 or n % 5 == 0:
		_sum += n

print(_sum)