f1 = 1
f2 = 2

sum = 2

target = 4000000
f = 0

while f < target:
	f = f2 + f1

	if f > target:
		break

	if f % 2 == 0:
		sum += f

	f1 = f2
	f2 = f

	print(f)

print(sum)