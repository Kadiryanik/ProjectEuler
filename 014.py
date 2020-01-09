def getStepNum(n):
	counter = 0
	while n != 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3 * n + 1
		counter += 1
	return counter

maxNum = 0
maxVal = 0
for i in range(1, 1000000):
	val = getStepNum(i)
	if maxVal < val:
		maxVal = val
		maxNum = i

print maxNum
print maxVal