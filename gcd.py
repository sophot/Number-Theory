# WRITTEN BY: KY SOPHOT
# BS.c Computer Science at Inha University in South Korea

'''
	This program find greatest common divisor of two numbers
	using Eucledean's Formula
'''
def gcd(a, b):
	ans = None
	smaller = None
	if a > b:
		remainder = a % b
		smaller = b
	else:
		remainder = b % a
		smaller = a

	if remainder == 0:
		ans = smaller
	else:
		ans = gcd(smaller, remainder)

	return ans


if __name__ == '__main__':
	a = int(input("input 1st number: "))
	b = int(input("input 2nd number: "))
	print(gcd(a, b))
	print("Nothing much")