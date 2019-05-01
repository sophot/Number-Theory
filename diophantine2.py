# WRITTEN BY: KY SOPHOT
# BS.c Computer Science at Inha University in South Korea

'''
	this program solve for all x, y solutions of
	DIOPHANTINE EQUATION aX + bY = N
'''

from diophantineEq import *


if __name__ == '__main__':
	a = 7
	b = 15
	N = 3
	g = diophantine(a, b)
	if N % g == 0:
		valXY[0] = valXY[0] * (int(N/g))
		valXY[1] = valXY[1] * (int(N/g))
		print( "%dx + %dy = %d  has solutions:" %(a, b, N))
		printAns(a, b)
	else:
		print("No Solution!!")
