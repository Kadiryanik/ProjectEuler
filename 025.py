a = 1
b = 1

i = 2
while 1:
	i += 1
	swap = b
	b = a + b
	a = swap

	if len(str(b)) == 1000:
		break

print i