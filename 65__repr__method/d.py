

#useful for debbugging

class Student:
	
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade
	def __repr__(self):
		return f"Student('{self.name}', '{self.grade}')"
		
mary = Student("Mary", "A+")

mary_string = repr(mary)
print(mary_string)

mary_object = eval(mary_string)
print("type mary_string ", type(mary_string))
print("type mary_object: ", type(mary_object))
print(mary_object.name)
print(mary_object)

