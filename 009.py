for a in range(1, 1000):
	for b in range(a, 1000):
		for c in range(b, 1000):
			if a + b + c == 1000:
				a2 = a * a
				b2 = b * b
				c2 = c * c
				if a2 + b2 == c2:
					print a * b * c
