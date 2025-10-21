
shapes = ("triangle", "square", "circle")

print(shapes)


#index        0           1       2
#         ('triangle', 'square', 'circle')

#tuples are ummutable
'''
shapes[1] = "rectangle"
shapes[1] = "rectangle"
    ~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''

print("length: ", len(shapes))


#its posssible to hae the same value in a tuple
shapes2 = ("circle", "square", "circle")
if "circle" in shapes2:
	print("circle is in tuple")

#loop to print a tuple 
for shape in shapes2:
	print(shape)

for i in range(len(shapes)):
	print(shapes[i])

print("*" * 25)

#tuple can have diferent types contents

mixed = ("string", 2, True, 2.5)
print(mixed)

#tuple with one item must have a coma(,) after
one_item = ("one", )
print("type(one_item): ", type (one_item))

#braquets are optional
multiple = 1,2,3,4,5
print("type(multiple): ", type(multiple))

#need braquetes if empty
empty = ()
print("type(empty): ", type(empty))

#unpacking tuples
names = ("Arthur", "Alice", "Gloria")
person1, person2, person3 = names

print("person1: ", person1,"\nperson2: ", person2, "\nperson3: ", person3)

#unpack to a list
numbers = (1,2,3,4,5,6,7,8)
n1, n2 , *rest = numbers

print("n1: ", n1,"\nn2: ", n2, "\nrest: ", rest)
print("types: \n", "\tn1: ", type(n1), "\n\tn2: ", type(n2), "\n\trest: ", type(rest))

#other example n1, n2 , *rest, n3 = numbers   -> n3 is the last number
numbers = (1,2,3,4,5,6,7,8)
n1, n2 , *rest, n3 = numbers

print("n1: ", n1,"\nn2: ", n2, "\nrest: ", rest, "\n\tn3: ", n3)
print("types: \n", "\tn1: ", type(n1), "\n\tn2: ", type(n2), "\n\trest: ", type(rest), "\n\tn3: ", type(n3))

#unpacking function

def function():
	return (1,2,3,4)
	
v1, v2,v3,v4 = function()

print("v1:",v1, ",v2:",v2, ",v3:",v3,",v4:",v4)

#join tuples
first = (1,2)
second = (3,4)
joined = first + second
print("joined: ", joined,"\ntype: ", type(joined))

multi = first * 3 # 3 tuples
print("multi: ", multi)
#how many time (1) occours in the tuple
print("one count: ", multi.count(1))

#print the index of the value
results = (12, 45, 34,16)
print("results: ", results)
print("result index of 34: ", results.index(34))


#casting
new_tuple = tuple([1,2,3])
print (new_tuple)
print("type new_tuple[0]: ", type(new_tuple[0]))


#technique to modify a tuple  #bcause its ummutable

values = (1,2,3)
print("id values: ", id(values))
temp_list = list(values)
temp_list[1] = 500
values = tuple(temp_list)
print("values: ", values)             #its a new tuple
print("id values: ", id(values))

#use negative index to access tuple itens
#index		0    1    2    3    4    5    6    7
letters = ("A", "B", "C", "D", "E", "F", "G", "H")
print("letter [-1]: ", letters[-1])
print("letter [-2]: ", letters[-2])
print("range: ", letters[1:4]) # >=1 <4 
print("range: ", letters[1:]) # from >=1 till end 
print("range: ", letters[:5]) # from beggining to <5

del letters
#print(letters)
'''    print(letters)
          ^^^^^^^
NameError: name 'letters' is not defined

'''

#even if an ummutable objet, its possible to modify a mutable item inside
simple_tuple = ([1,3], 2,3)
print(simple_tuple)
print("type simple_tuple: ", type(simple_tuple),"\ntype simple_tuple[0]: ", type(simple_tuple[0]))
simple_tuple[0].append(55)
print(simple_tuple)


"""
('triangle', 'square', 'circle')
length:  3
circle is in tuple
circle
square
circle
triangle
square
circle
*************************
('string', 2, True, 2.5)
type(one_item):  <class 'tuple'>
type(multiple):  <class 'tuple'>
type(empty):  <class 'tuple'>
person1:  Arthur 
person2:  Alice 
person3:  Gloria
n1:  1 
n2:  2 
rest:  [3, 4, 5, 6, 7, 8]
types: 
 	n1:  <class 'int'> 
	n2:  <class 'int'> 
	rest:  <class 'list'>
n1:  1 
n2:  2 
rest:  [3, 4, 5, 6, 7] 
	n3:  8
types: 
 	n1:  <class 'int'> 
	n2:  <class 'int'> 
	rest:  <class 'list'> 
	n3:  <class 'int'>
v1: 1 ,v2: 2 ,v3: 3 ,v4: 4
joined:  (1, 2, 3, 4) 
type:  <class 'tuple'>
multi:  (1, 2, 1, 2, 1, 2)
one count:  3
results:  (12, 45, 34, 16)
result index of 34:  2
(1, 2, 3)
type new_tuple[0]:  <class 'int'>
id values:  251544044534848
values:  (1, 500, 3)
id values:  251544044534656
letter [-1]:  H
letter [-2]:  G
range:  ('B', 'C', 'D')
range:  ('B', 'C', 'D', 'E', 'F', 'G', 'H')
range:  ('A', 'B', 'C', 'D', 'E')
([1, 3], 2, 3)
type simple_tuple:  <class 'tuple'> 
type simple_tuple[0]:  <class 'list'>
([1, 3, 55], 2, 3)
"""



