vals = [ 0 ]
sum = 0

for i in range(1, 10):
	vals.append(i ** 5)

for i in range(10, 1000000):
	x = 0
	num = i
	while num > 0:
		x += vals[num % 10]
		num /= 10
	if x == i:
		#print i
		sum += i
print sum
