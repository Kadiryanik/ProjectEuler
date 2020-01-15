"""
    a stores a * 10 % b, for next A
    A      b = A / b
    10  /  7 = 1 <--
    30  /  7 = 4
    20  /  7 = 2
    60  /  7 = 8
    40  /  7 = 5
    50  /  7 = 7
    10  /  7 = 1 <--

    a = (5 * 10) % 7 = 1, end condition for 7
    this code trys to get a == 1 equality
    you can debug in this format with enabling print in while loop 
"""
def getLen(b):
    a = 1
    t = 0

    while t < b: # t cant be bigger than b, for 7, maximum t value is 6.
        A = a % b * 10
        a = a * 10 % b
        t += 1

        #print "  " + str(A) + " / " + str(b) + " = " + str(A / b)
        if a == 1:
            return t
    # if reach here we have smallest cycle 1,1(6) or something like that.
    # Or we have 2, 5 in number which breaks this algorithm. Ignoring them.
    return 0

MAX = 0
MAX_NUM = 0
for i in range(1000, 0, -1):
    ret = getLen(i)
    if ret > MAX:
        MAX = ret
        MAX_NUM = i
        if ret == i - 1: #for "i", maximum value of "ret" is equals "i - 1"
            """
                so if we reach here mean next numbers' "ret" value which lower than "i"
                can't be grether than this MAX. We can break loop.
            """
            break
    #print str(i) + " -> " + str(ret)

print "result: " + str(MAX_NUM) + " -> " + str(MAX)
