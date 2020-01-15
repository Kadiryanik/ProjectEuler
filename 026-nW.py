# not working will improve
def checkSimilarity(S, n):
	for startPoint in range(0, len(S) / 2):
		s = S[startPoint:]
		for i in range(len(s) / 2, 0, -1):
			if s[0:i] == s[i:len(s)]:
				print str(n) + "-> 0," + S[0:startPoint] + "(" + s[0:i] + ") = " + str(i)
				return i # return with addition startPoint to print correct string
	return 0

def getFloat(n):
	divisionArr = []
	remaining = 1
	if n > 99:
		remaining = 10

	lastRemaining = 9
	sameValCounter = 0
	while remaining != 0:
		remaining = remaining * 10
		division = remaining / n
		remaining = remaining - (division * n)

		divisionArr.append(str(division))
		#print ("remaining: {0} division: {1}".format(remaining, division))

		# check 1,1666... cycle
		if lastRemaining == remaining:
			sameValCounter += 1
			if sameValCounter > 20: # 20 digit same so it
				print str(n) + "-> 0,".join(divisionArr[0:len(divisionArr) - 101]) + "(" + divisionArr[len(divisionArr) - 100] + ") = 1"
				return 1
		else:
			lastRemaining = remaining

		s = "".join(divisionArr)
		ret = checkSimilarity(s, n)
		if ret != 0:
			return ret

	print str(n) + "-> 0," + "".join(divisionArr[0:len(divisionArr)])
	return 0

biggestVal = 0
biggestNum = 0
for i in range(983, 984):
	ret = getFloat(i)
	if biggestVal < ret:
		biggestVal = ret
		biggestNum = i

print ""
print str(biggestNum) + " -> " + str(biggestVal)
