# https://www.index.dev/blog/how-to-check-python-variable-types
# portfolio courses https://www.youtube.com/@PortfolioCourses

price = 50
shipping = 10.50
total = price + shipping

print (total)

tax_rate = 1.15
total = total * tax_rate

print(total)

customer_name = "Idris Elba"
discount = False

print("variable type:", "price:", type(price), "total:", type(total))

a = 5
b = 8.2
c  = "Hello world"
d = [1, 2, 3, 4]
e = (1, 2, 3)
f = {'a': 1, 'b': 2}

'''
The type() function is very simple and easy to use.
It returns the type of variable, 
which can help you understand the kind of data you are working with.
Just keep in mind that it does not provide more detailed type checking,
such as checking for subclasses.
'''

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

"""
The isinstance() function is more flexible than type()
because it considers inheritance. For example,
if you have a subclass, isinstance()
will return True for checks against both the subclass and the parent class.
"""
print("**********")
print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, str))
print(isinstance(d, list))

class Animal:
	pass

class Dog(Animal):
	pass

dog = Dog()

print("**********")
print(isinstance(dog, Animal))
print (isinstance(dog, Dog))
#using type() and isinstance()
print("**********")
print(type(dog) == Dog)			#output True
print(type(dog) == Animal)		#output False
print (isinstance(dog, Dog))	#output True
print(isinstance(dog, Animal))	#output True

'''
Use type(): When you need to check if an object is exactly of a specific type and not a subclass.
Use isinstance(): When you want to check if an object is an instance of a class or any subclass thereof.
'''

print("**********")
"""
With the introduction of type hints in Python 3.5 and later, 
you can provide hints about the types of variables and function return values,
 improving code readability and aiding static analysis tools.
"""
# type hinting with variables

def add(x: int, y: int) -> int:
	return (x + y)

result = add(5, 6)
print("result:", result, type(result))

result2 = add("hello", "Filipe")
print ("result2:", result2, type(result2))
print("**********")


'''
Type hints do not enforce type checking at runtime but serve as a guide for developers and tools.
 They can be checked using tools like mypy for static type checking.
'''
a: int = 3
b: float = 20.3

print (type(a))
print (type(b))

print("*********")
"""
Python's typing module provides support for type hints and helps in creating more
 complex types, like lists of specific types, tuples, and more.
"""

from typing import List, Tuple, Dict

# Using typing for more complex types

def process_list(numbers: List[int]) -> int:
	return (sum(numbers))
  
def get_coordinates() -> Tuple[float, float]:
	return (1.0, 2.0)

def get_user_info() -> Dict [str, int]:
	return ({'age' : 30, 'id' : 123})

# Using the functions with typing
print(process_list([1, 2, 3]))
print(get_coordinates())      
print(get_user_info())

"""
The typing module allows for more complex type definitions,
 improving the readability and maintainability of your code.
 It is especially useful in larger codebases where understanding
 data structures at a glance is beneficial.
"""

