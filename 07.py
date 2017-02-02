#~ 07. Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
#~ Please write a program to print some Python built-in functions documents, such as abs(), int(), input() and add document for your own function.

def myFunc(a,b):
'''
Takes two numbers as argument and returns their sum.
'''
	return a+b

if __name__ == '__main__':
	print(abs.__doc__)
	print(int.__doc__)
	print(input.__doc__)

	print(myFunc(5,8))
	print(myFunc.__doc__)
