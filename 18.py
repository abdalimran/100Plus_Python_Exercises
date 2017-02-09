#~ 18. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#~ Suppose the following input is supplied to the program:
#~ 9
#~ Then, the output should be:
#~ 11106

#~ Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

def main():
	a = input()
	result = int(a)+int((a*2))+int((a*3))+int((a*4))
	print(result)


if __name__=="__main__":
	main()
