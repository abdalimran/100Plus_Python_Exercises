#~ 02. Write a program which can compute the factorial of a given number.
#~ Suppose the following input is supplied to the program:
#~ 8
#~ Then, the output should be:
#~ 40320

def Factorial(num):
	if(num == 0):
		return 1
	else:
		return num * Factorial(num-1)

if __name__ == '__main__':
	num = eval(input())
	print(Factorial(num))
