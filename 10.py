#~ 10. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

#~ Suppose the following inputs are given to the program:
#~ 3,5
#~ Then, the output of the program should be:
#~ [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

def Main():
	dimensions = [int(x) for x in input().split(',')]
	
	rows = dimensions[0]
	columns = dimensions[1]
	
	list2d = [[0 for col in range(columns)] for row in range(rows)]
	
	for i in range(rows):
		for j in range(columns):
			list2d[i][j] = i*j
			
	print(list2d)
	
	
if __name__ == '__main__':
	Main()
