#~ 12. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#~ Suppose the following input is supplied to the program:
#~ Hello world
#~ Practice makes perfect
#~ Then, the output should be:
#~ HELLO WORLD
#~ PRACTICE MAKES PERFECT

#~ Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

def main():
	lines = eval(input("Enter number of lines: "))
	
	seq_lines = []
	
	for i in range(lines):
		seq_lines.append(input().upper())
	
	for i in seq_lines:	
		print(i)

if __name__=='__main__':
	main()
