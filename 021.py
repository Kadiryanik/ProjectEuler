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

amicableNums = []
num = 2

while num < 10000:
	print num
	
	if num in amicableNums:
		print str(num) + " already calculated!"
	else:
		divSum = d(num)
		if num == d(divSum) and num != divSum:
			amicableNums.append(num)
			amicableNums.append(divSum)

	num += 1

print amicableNums
print sum(amicableNums)