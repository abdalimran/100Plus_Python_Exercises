#~ 05. Write a method which can calculate square value of number.

def SquareValue(n):	
	return n**n
	
if __name__ == '__main__':
	n = eval(input("Enter a value: "))
	print(SquareValue(n))
