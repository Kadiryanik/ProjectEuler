def fact(n):
	for i in range(1, n):
		n *= i
	return n

val = 0
for i in str(fact(100)):
	val += int(i)
print val