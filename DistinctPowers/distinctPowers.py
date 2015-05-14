numRange = 101
powerList = []

for a in range(2, numRange):
	for b in range(2, numRange):
		power = a ** b
		if power not in powerList:
			powerList.append(power)

print(len(powerList))
