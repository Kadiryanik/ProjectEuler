# grid size
UPLIMIT = 20
UPLIMIT_PRODUCT_2 = UPLIMIT * 2

counter = 0

# initilize the binarys with given UPLIMIT
startVal = "0" * UPLIMIT
startVal += "1" * UPLIMIT
endVal = startVal[::-1]

# set formatter for int to binary
formatter = "{0:0" + str(UPLIMIT * 2) + "b}"

# increment the number from start to end point
for i in xrange(long(startVal, 2), long(endVal, 2) + 1):
	binary = formatter.format(i)

	# if possible to reach end point increment the counter, print the path
	zeros = binary.count('0')
	ones = UPLIMIT_PRODUCT_2 - zeros
	if zeros == ones:
		counter += 1
		# print binary

print counter