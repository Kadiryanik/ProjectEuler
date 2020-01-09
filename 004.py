def isPalindrome(s):
	reverse = s[::-1]
	if s == reverse:
		return 1
	return 0

max = 0
maxI = 0
maxJ = 0
for i in range(999, 100, -1):
	for j in range(999, 100, -1):
		if isPalindrome(str(i * j)):
			if max < i * j:
				max = i * j
				maxI = i
				maxJ = j
print(str(maxI) + " * " + str(maxJ) + " = " + str(max))
