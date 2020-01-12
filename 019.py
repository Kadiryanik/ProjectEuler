#mountsDict = { "January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31 }
mountsDayCounts = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

day = 6 # 1 Jan 1901 = Tuesday, start on sunday
sundays = 0

for i in range(1901, 2001):
	if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
		mountsDayCounts[1] = 29
	else:
		mountsDayCounts[1] = 28

	print "year: " + str(i)
	print "mounts: ",
	for j in range(0, 12):
		while day <= mountsDayCounts[j]:
			if(day == 1):
				print (j + 1),
				sundays += 1
			day += 7		
		day = day % mountsDayCounts[j]
  	print ""
print sundays