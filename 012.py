import math

lastAdded = 1
num = 1
while 1:
	lastAdded += 1
	num += lastAdded

	counter = 0
	#print str(num) + " -> ",
	for i in range(1, int(math.sqrt(num)) + 1):
		if num % i == 0:
			#print i,
			counter += 2
	#print str(num)

	if counter > 500:
		break

print num
