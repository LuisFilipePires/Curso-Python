



x = True
y = False

print ("type: ", "\n\tx: ", type(x), "\n\ty: ", type(y))

result = 3 > 5

print("result: ", result)    #False 

result2 = True or False

print("result2: ", result2)   #True

result = 5 in [1,2,3,]
print("result: ", result)   #False

result = 1 is 1
print("result: ", result) # True



#if condition  is a boolean
a = 2
b = 3

if (a <= b):
	print("a <= b")
else:
	print("a > b")
	
	
convert = bool(1)
print("convert: ", convert)    #True

'''
	by default most values are True
	
	False values include:
		-the number 0 ( or 0.0, 0j)
		-(empty) strings, lists, tuples, sets,
		 dictionaires, ranges
		-none
'''
convert = bool("")
print("convert: ", convert)    #False

if (""):
	print("string is not empty")
else:
	print("String is empty")
#String is empty

	
'''
by default an object is considerated True
unless its class definesneither a __bool__()
method that returns a False or a __len__()
method tha returns zero, when called with the object
'''

class Car:
	def __init__(self):
		self.fuel = 0
	
	def __bool__(self):
		return self.fuel > 0

car = Car()

if car:
	print("Fuel is not empty")
else:
	print("Fuel is empty")
#Fuel is empty


