# WRITTEN BY: KY SOPHOT
# BS.c Computer Science at Inha University in South Korea

'''
	This program find least common muliply of two numbers
'''
from gcd import *

def lcm(a, b):
	ans = b * (a / gcd(a, b))
	print(int(ans))


##### MAIN #####
if __name__ == "__main__":
	a = int(input("input 1st number"))
	b = int(input("input 2nd number"))
	lcm(a,b)