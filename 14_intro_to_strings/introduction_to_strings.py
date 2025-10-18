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



