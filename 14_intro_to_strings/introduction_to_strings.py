programmer = "Grace Hopper"
print(programmer)
print("type programmer: ", type(programmer))

computer = 'Havard Mark 1'
print("type computer: ", type(computer))

quote1 = """
The ship in port is safe
but that's not what ships
are built for
"""

print (quote1)
print("type (quote1): ", type(quote1))

quote2 = '''
it's yeaser to ask
forgiveness than it is to
get permission
'''

print(quote2)
print("type (quote2): ", type(quote2))

school = "yale university"
print("school: ", school)
print("school [0] index: ", school[0])  
print("type(school[0]): ", type(school[0]))

print("school[5]: ", school[5])
print("school[0:4]: ", school[0:4])
#print from
print("school[5:]: ", school[5:])

print("len(school): ", len(school))

other_string = "Vassar college"

if (school == other_string) :
	print("Schools are the same")
else:
	print("Schools are NOT the same") 


text = "invented one of the 1th linkers"

for character in text:
	print(character)

for character in text:
	print(character, sep=",", end="")

print("")

count = 0
for character in text:
	if(character == "e"):
		count+=1
print("e count: ", count)

if ("one" in text):
	print("one IS  in text")

if ("two" not in text):
	print("two is NOT in text")

birth = "    Born In New York City  "
print(birth.upper())
print(birth.lower())
print(birth.strip())
print(birth.replace("York", "Fork"))
print(birth.split())

first_name = "Grace"
last_name = "Hopper"
full_name = first_name + " " + last_name
print(full_name)
print("adress first name: ", hex(id(first_name)))

print("hex(id(last_name)):", hex(id(last_name)))
print("hex(id(full_name)): ", hex(id(full_name)))

print("Line One\nLine 2")

person1 = "Hector"
person2 = person1

print("hex(id(person1)): ", hex(id(person1)))
print("hex(id(person2): ", hex(id(person2)))

 
birthday = "Born in the year {}"
print("format to 1980: ", birthday.format(1980))

#multiple placeholders {}

text2 = "{} how are {} {}"
print(text2.format("Hello", "you", "today?"))


"""
output:

Grace Hopper
type programmer:  <class 'str'>
type computer:  <class 'str'>

The ship in port is safe
but that's not what ships
are built for

type (quote1):  <class 'str'>

it's yeaser to ask
forgiveness than it is to
get permission

type (quote2):  <class 'str'>
school:  yale university
school [0] index:  y
type(school[0]):  <class 'str'>
school[5]:  u
school[0:4]:  yale
school[5:]:  university
len(school):  15
Schools are NOT the same
i
n
v
e
n
t
e
d
 
o
n
e
 
o
f
 
t
h
e
 
1
t
h
 
l
i
n
k
e
r
s
invented one of the 1th linkers
e count:  5
one IS  in text
two is NOT in text
    BORN IN NEW YORK CITY  
    born in new york city  
Born In New York City
    Born In New Fork City  
['Born', 'In', 'New', 'York', 'City']
Grace Hopper
adress first name:  0xe9405d58b030
hex(id(last_name)): 0xe9405d58b0c0
hex(id(full_name)):  0xe9405d531ef0
Line One
Line 2
hex(id(person1)):  0xe9405d58b510
hex(id(person2):  0xe9405d58b510
format to 1980:  Born in the year 1980
Hello how are you today?

"""


