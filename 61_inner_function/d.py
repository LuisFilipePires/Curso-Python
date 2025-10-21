
#inner function can access variables inside the scope

def outer():
	
	def inner():
		print("Inner function")
		print("y: ", y)
		#print("z: ", z)  #NameError: cannot access free variable 'z' 
						 #where it is not associated with a value in enclosing scope

	y = 3        # y is defined before call inner()
	inner()
	#z = 5

outer()


#variables inside each scope belongs to then
#nonlocal   definition

def outer1(x):
	y = 5          #
	print("first y: ", y, "      id y: ", id(y))
	b = 44
	print("first b: ", b, "    id b: ", id(b))
	def inner(z):
		y = 50     # not the same y variable
		nonlocal b # b is the same variables
		b = 77
		print ("y: ", y)
		print("inner y: ", y, "    id y: ", id(y)) 
		print("inner b: ", b, "     id b: ", id(b))
	inner(10)
	print("y: ", y)
	print ("b: ", b, "    id b: ",  id(b))

outer1(2)
	
	
