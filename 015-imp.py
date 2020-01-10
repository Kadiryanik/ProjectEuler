"""
	Improved Solution
	
	# 1 mean Go Down, 0 mean Go Rigt

	Grid Size = 3
		00001111 Start
		00010111
		00011011
		00011101
		00011110
		...
		11000011
		11000101
		11000110
		11001001
		11001010
		11001100
		11010001
		11010010
		11010100
		11011000
		11100001
		11100010
		11100100
		11101000
		11110000 End

	split binary into LEFT and RIGHT
	increment LEFT side and check possible combinations for RIGHT side

		LEFT -> RIGHT combinations count
		0001 -> 4
		0010 -> 4
		0011 -> 6
		0100 -> 4
		0101 -> 6
		0110 -> 6
		0111 -> 4

	then repeats so we dont need to check more, just multiply with 2
		1000 -> 4
		...

	result = 2 * (4 + 4 + 6 + 4 + 6 + 6 + 4) + 2 = 70
"""

# grid size
UPLIMIT = 20

# set formatter for int to binary
formatter = "{0:0" + str(UPLIMIT) + "b}"

def calculate(b):
	counter = 0
	for i in xrange(1, (2 ** UPLIMIT) - 1):
		binary = b
		binary += formatter.format(i)

		# if possible to reach end point increment the counter, print the path
		zeros = binary.count('0')
		ones = (2 * UPLIMIT) - zeros
		if zeros == ones:
			counter += 1
			# print binary # for debug combinations
	return counter

# define and set zeros to calculatedVals
calculatedVals = [0] * UPLIMIT

# counter for possible ways
counter = 0

# increment the LEFT side bits, 1 to UPLIMIT/2 and add RIGT side combination count to counter
for i in xrange(1, (2 ** UPLIMIT) / 2):
	binary = formatter.format(i)

	zeros = binary.count('0')
	ones = UPLIMIT - zeros
	if calculatedVals[ones] == 0:
		result = calculate(binary)
		# set symetric vals
		calculatedVals[ones] = result
		calculatedVals[UPLIMIT - ones] = result

	counter += calculatedVals[ones]
	# print binary + " -> " + str(calculatedVals[ones]) # for debug vals

# * 2: we look for half of LEFT side so multiply 2
# + 2: start and end binary series
print counter * 2 + 2