import math

def d(n):
	divisorsSum = -n # 1 * n will added so we need to delete n

	uplimit = int(math.sqrt(n))
	if(uplimit ** 2 == n):
		divisorsSum += uplimit
	else:
		uplimit += 1

	for i in range(1, uplimit):
		if n % i == 0:
			# these loop contain a, where a <= b in a * b multiplication
			# so we add a and b
			divisorsSum += i + (n / i)
	
	return divisorsSum

UPLIMIT = 28123
abundantNums = []

# get abundantNums
for num in range(1, UPLIMIT):
	if num < d(num):
		abundantNums.append(num)

# set numbers
vals = [i for i in range(0, UPLIMIT)]

arrayLen = len(abundantNums)
for i in range(0, arrayLen):
	for j in range(i, arrayLen):
		if abundantNums[i] + abundantNums[j] < UPLIMIT:
			# set 0 to abundantNums
			vals[abundantNums[i] + abundantNums[j]] = 0
		else:
			break

# get sum of non abundantNums
result = sum(vals)
print result