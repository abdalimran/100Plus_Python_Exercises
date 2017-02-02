#~ 09. Write a program that calculates and prints the value according to the given formula:
#~ Q = Square root of [(2 * C * D)/H]
#~ Following are the fixed values of C and H:
#~ C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence.

from math import sqrt

def Main():
	c = 50.0
	h = 30.0
	d = [int(x) for x in input().split(',')]
	
	q = []
	
	for i in d:
		q.append(round(sqrt((2*c*i)/h)))
	
	print(q)

if __name__ == "__main__":
	Main()
