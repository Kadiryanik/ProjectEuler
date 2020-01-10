FIRST_SET = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
SECOND_SET = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def getName(n):
	result = ""
	while n != 0:
		if n > 0 and n < 21:
			result += FIRST_SET[n]
			n = 0
		elif n > 20 and n < 100:
			result += SECOND_SET[n / 10] + FIRST_SET[n % 10]
			n = 0
		elif n == 1000:
			result += "onethousand"
			n = 0
		elif n % 100 == 0:
			result += FIRST_SET[n / 100]
			result += "hundred"
			n = 0
		elif n > 100 and n < 1000:
			result += FIRST_SET[n / 100] + "hundredand"
			n = n % 100
	return result

result = 0
for i in range(1, 1001):
	name = getName(i)
	val = len(name)
	result += val
	print name + "->" + str(val)

print result