#~ 20. Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
#~ D 100
#~ W 200
#~ D means deposit while W means withdrawal.

#~ Suppose the following input is supplied to the program:
#~ D 300
#~ D 300
#~ W 200
#~ D 100
#~ Then, the output should be:
#~ 500

#~ Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


def main():
	net_amount = 0
	
	while True:
		transaction = input().split(" ")
		
		if transaction == [""]:
			break
			
		if transaction[0] == "D":
			net_amount += int(transaction[1])
		elif transaction[0] == "W":
			net_amount -= int(transaction[1])
	
	print("Net amount: {}".format(net_amount))


if __name__=="__main__":
	main()
