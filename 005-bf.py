UPLIMIT = 21
found = 0
num = (1 * 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19) - 1

while found == 0:
	found = 1
	num += 1
	print num
	for i in range(2, UPLIMIT):
		if num % i != 0:
			found = 0
			break
print num
