# WRITTEN BY: KY SOPHOT
# BS.c Computer Science at Inha University in South Korea

'''
	this program solve for all x, y solutions of
	DIOPHANTINE EQUATION aX + bY = gcd(a, b)
'''
from gcd import *
valXY = [1, 1]
COUNT = 1
SECOND_RUN = 1

def diophantine(a, b):
	valXY[0] = 1
	valXY[1] = 1
	x = 1
	ans = None
	newA = None
	if a > b:
		y = int(a/b)
		remainder = a % b
		newA = b
	else:
		y = int(b/a)
		remainder = b % a
		newA = a

	if remainder == 0:
		ans = newA
		global SECOND_RUN
		if SECOND_RUN == 1:
			valXY[1] = y-1
	else:
		SECOND_RUN += 1
		ans = diophantine(newA, remainder)

		global COUNT
		# print("y = ", y)
		tempX = valXY[0]
		valXY[0] = (x * valXY[1])			#X
		if (COUNT == 1):
			valXY[1] = (valXY[1] * y)	#Y
			COUNT += 1
		else:
			valXY[1] = (valXY[1] * y) + tempX	#Y
		# print("X=",valXY[0],"Y=",valXY[1])
	return ans
#END OF dophantine

def printAns(a, b):
	g = gcd(a, b)
	if b > a:
		temp = valXY[0]
		valXY[0] = valXY[1]
		valXY[1] = temp

	if a*getX() > b*getY():
		valXY[1] =  -valXY[1]
	else:
		valXY[0] =  -valXY[0]

	print( "x = %d + %dt" % (getX(), int(b/g)) )
	print( "y = %d - %dt" % (getY(), int(a/g)) )
##END OF printAns

def getX():
	return valXY[0]

def getY():
	return valXY[1]


##### MAIN #####
if __name__ == "__main__":
	a = 7
	b = 15
	g = diophantine(a, b)
	print( "%dx + %dy = %d { gcd(%d, %d) } has solutions:" %(a, b, g, a, b))
	printAns(a, b)


