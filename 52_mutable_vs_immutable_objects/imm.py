


x = 4

y = x

print("id(x): ", id(x))
print("id(y): ", id(y))
x = x + 2  #  x + 2 its a new object

print("x :", x)
print("id(x): ", id(x))
print("id(y): ", id(y))

print("*" * 20)

text = "abc"
print("id(text): ", id(text))

text = text + "123"
print("text: ", text)
print("id(text): ", id (text))

numbers = [1,2,3]
print("numbers: ", numbers)
print("id(numbers): ", id(numbers))
numbers.append(4)
print("numbers: ", numbers)
print("id(numbers): ", id(numbers))

'''
id(x):  11646408    ummutable object
id(y):  11646408
x : 6
id(x):  11646472
id(y):  11646408
********************
id(text):  11464128
text:  abc123
id(text):  251348010837280
numbers:  [1, 2, 3]
id(numbers):  251348012157760    mutable object
numbers:  [1, 2, 3, 4]
id(numbers):  251348012157760
'''

tuple_with_list = ([1,2], 5,6)
print(tuple_with_list)
print("id: ", id(tuple_with_list))

tuple_with_list[0].append(2)
print(tuple_with_list)
print("id: ", id(tuple_with_list))

#list is mutable
#but tuple is ummutable
'''
tuple_with_list[0] = [3,6]
    tuple_with_list[0] = [3,6]    #can not assigne a new list to 
									#tuple cause tuple is ummutable
    ~~~~~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment

'''


'''
mutable:

	lists
	dictionaires
	sets
	*user_defined_classes
	 *ultimately decided by class definition

ummutable
	numbers ( integer, float,etc)
	tuples
	strings
	frozen sets
'''

def add(m):
	print("id(m): ", id(m))
	m = m + 1
	print("id(m): ", id(m))
	
def add2(m):
	print("id(m): ", id(m))
	m = m + 1
	print("id(m): ", id(m))
	return (m)
	
y = 5

print("id(y): ", id(y))
add(y)
print(y)  # 5  # y is passed by reference

print("id(y): ", id(y))
y = add2(y)
print("y = add2(y): ", y)
print("id(y): ", id(y))
'''
id(y):  11646440
id(m):  11646440
id(m):  11646472
5
id(y):  11646440
id(m):  11646440
id(m):  11646472
y = add2(y):  6
id(y):  11646472

'''

def add_to_list(letters):
	letters.append('X')
	print("id(letters): ", id(letters))

uppercase = ["A","B","C"]
add_to_list(uppercase)
print(uppercase)
print("id(uppercase): ", id(uppercase))
	
