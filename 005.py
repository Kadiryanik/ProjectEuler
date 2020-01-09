UPLIMIT = 21
vals = [1] * UPLIMIT
for i in range(2, UPLIMIT):
	num = i
	for j in range(2, i):
		max = 0
		while num % j == 0:
			num = num / j
			vals[i] = 0;
			max += 1
		if vals[j] < max:
			vals[j] = max
			vals[i] = 0
result = 1
for i in range(2, UPLIMIT):
	if vals[i] != 0:
		a = 1
		#print (str(i) + "->" + str(vals[i]))
	for j in range(0, vals[i]):
		result = result * (i)

print result
