
#nonlocal keyword
#allow to modify a variable inside a scope

def outer():
	enclosing_scope_variable = 10
	
	def inner():
		nonlocal enclosing_scope_variable
		enclosing_scope_variable = 20
		print("inner: ", enclosing_scope_variable)
	
	inner()
	print("outer : enclosing: ", enclosing_scope_variable)

outer()
