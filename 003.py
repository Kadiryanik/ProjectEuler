import math

def checkPrimeFactor(n, i):
	while n % i == 0:
		print i
		n = n / i
	return n
def primeFactors(n):
	n = checkPrimeFactor(n, 2)

	for i in range(3, 1 + int(math.sqrt(n)), 2):
		n = checkPrimeFactor(n, i)
	if n > 2:
		print n

primeFactors(600851475143)	
