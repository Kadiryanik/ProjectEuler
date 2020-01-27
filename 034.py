facts = []
for i in range(0, 10):
	fact = 1
	num = i
	while num > 0:
		fact *= num
		num -= 1
	facts.append(fact)


#UPLIMIT value calculation ref: https://www.xarg.org/puzzle/project-euler/problem-34/
UPLIMIT = 1499999 
total = 0
for i in range(3, UPLIMIT):
	sum = 0
	num = i
	while num > 0:
		sum += facts[num % 10]
		num /= 10
	if sum == i:
		total += i
		#print i

print total
