vals = []
UPLIMIT = 101

for a in range(2, UPLIMIT):
	x = a
	for b in range(2, UPLIMIT):
		x *= a
		if x not in vals:
			vals.append(x)

print len(vals)
