


class Student:
	
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade
	def __str__(self):
		return f"{self.name} ({self.grade})"
	#def __repr__(self):  #for debugg 

mary = Student("Mary", "A+")

print(mary)

mary_string = str(mary)
print (mary_string)
