#~ 16. Write a program that accepts a sentence and calculate the number of letters and digits.
#~ Suppose the following input is supplied to the program:
#~ hello world! 123
#~ Then, the output should be:
#~ LETTERS 10
#~ DIGITS 3

#~ Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

def main():
	sentence = input()
	letters = 0
	digits = 0
	
	for ch in sentence:
		if ch.isalpha():
			letters +=1
		elif ch.isdigit():
			digits +=1
	
	print("Letters: {}\nDigits: {}".format(letters, digits))

if __name__=="__main__":
	main()
