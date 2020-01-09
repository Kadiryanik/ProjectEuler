import math

sum = 2
for i in range(3, 2000000, 2):
	prime = 1
	for j in range(3, 1 + int(math.sqrt(i))):
		if i % j == 0:
			prime = 0
			break

	if prime == 1:
		sum += i
print sum
