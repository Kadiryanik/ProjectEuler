PASS_COUNT = 2
X = 0

SUM = 1
i = 3
while i < (1001 * 1001) + 1:
	#print i
	SUM += i
	X += 1
	
	if X == 4:
		X = 0
		PASS_COUNT += 2
	i += PASS_COUNT
	
print SUM
