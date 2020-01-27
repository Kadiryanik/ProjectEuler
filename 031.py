# ways keeps how many combination can write for index
# ways[5] = 4 mean: 5p combinations num equals 4 [ (1p + 2x2p), (3x1p + 2p), (5x1p), (5p) ]
# for debug, set target = 10, coins = [ 1, 2, 5, 10 ] and enable print
target = 200
coins = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
ways = [ 0 ] * (target + 1)
ways[0] = 1;

for c in coins:
	for j in range(c, target + 1):
		ways[j] += ways[j - c]
		#print "ways[" + str(j) + "] += ways[" + str(j) + " - " +str(c) + "] = " + str(ways[j])

print ways[-1]
