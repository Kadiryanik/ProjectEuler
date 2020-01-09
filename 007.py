import math

primeCount = 3
num = 3
while 1:
	num += 2
	prime = 1
	for i in range(2, 1 + int(math.sqrt(num))):
		if num % i == 0:
			prime = 0
			break
	if prime == 1:
		if primeCount == 10001:
			break
	
		primeCount += 1
print num
