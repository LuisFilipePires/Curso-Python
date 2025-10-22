

global x
x = 20

def function():
	global x
	x = 10
	print("x function", x)
	global new_variable
	new_variable  = 200
	
	def inner():
		global x
		x = 57
		print("inner x: ", x)
	inner()
	


#print("new_variable: ", new_variable) ----->ERROR caled before created
function()

print("x outside: ", x)
print("new_variable: ", new_variable)
'''
x function 10
inner x:  57
x outside:  57
new_variable:  200
'''
