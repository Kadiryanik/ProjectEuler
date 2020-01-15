from math import sqrt

def isPrime(num):
	if num < 2:
		return 0
	for i in range(2, 1 + int(sqrt(num))):
		if num % i == 0:
			return 0
	return 1

MAX = 0
for a in range(-999, 1000):
	for b in range(-999, 1000):
		n = 0
		while isPrime(n * n + a * n + b):
			n += 1
		if n > MAX:
			MAX = n
			print "n^2 + ({0})n + ({1}) = {2}".format(a, b, n)