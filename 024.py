from itertools import permutations
p = list(permutations("0123456789"))[999999]

result = ""
for i in p:
	result += i
print result
