#~ Define a class, which have a class parameter and have a same instance parameter.

class Person:
	# Defining a class parameter "name"
	name = "Person Name"
	
	def __init__(self, name = None):
		# self.name is the instance parameter
		self.name = name

if __name__ == "__main__":
	obj1 = Person("Abdullah")
	print("%s : %s" %(Person.name, obj1.name))

	obj2 = Person("Imran")
	print("%s : %s" %(Person.name, obj2.name))
