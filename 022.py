textFile = open("/home/sadnes/Desktop/p022_names.txt", "r")
words = sorted(textFile.read().split(","))
words = [w[1:len(w) -1] for w in words]

def getSum(n):
	sum = 0
	for i in n:
		sum += (ord(i) - 64)
	return sum

realSum = 0
for i, w in enumerate(words):
	realSum += ((i + 1) * getSum(w))

print realSum