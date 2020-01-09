numX = 0
numY = 1
sum = 0

while 1:
	swap = numX
	numX = numY
	numY += swap

	if numY > 4000000:
		break
	if numY % 2 == 0:
		sum += numY
print sum
