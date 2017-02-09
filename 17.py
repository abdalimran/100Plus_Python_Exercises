#~ 17. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#~ Suppose the following input is supplied to the program:
#~ Hello world!
#~ Then, the output should be:
#~ UPPER CASE 1
#~ LOWER CASE 9

#~ Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

def main():
	sentence = input()
	result = {'uppercase' : 0,'lowercase' : 0}
	
	for ch in sentence:
		if ch.isupper():
			result['uppercase'] += 1
		elif ch.islower():
			result['lowercase'] += 1
	
	print("Upper case: {} \nLower case: {}".format(result['uppercase'],result['lowercase']))
	
	
if __name__=="__main__":
	main()
