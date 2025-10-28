
import copy

student = ["Grace Hooper", 22.5, 7]

print(student[0])

student1 = {
	"name" : "Grace Hooper",
	"age" : 22,
	"gpa" : 7
}

print (student1)
print(len(student1))
print(type(student1))

trybools = {False : [1,2,3], True: [4,5,6]}
print(trybools)

ada = dict(name = "Ada", gpa = 3.7)
print(ada)

empty_dictionary = {}
print (empty_dictionary)

course = {
	"name" : "python 80",
	"average" : 8.5
}

print(course["name"])
print(course.get("average"))
course['average'] = 98
print (course["average"])

course ["room number"] = 45 
print(course)

course.update ({"name": "python 102", "average" : 99, "teacher" : "Barbara"})
print(course)

variable = course        # referency to the same 
variable["teacher"] = "Selena"
print (course)

course_copy = course.copy()
course_copy["teacher"] = "Luis"
print("course: ", course)
print("course_copy: ", course_copy)


for key in course:
	print (key, course[key])
	
school = {
	"name" : "Havard",
	"city" : "Cambridge",
	"country" : "usa"
}

school["founded"] = 1936
print(school)

school.popitem()
print(school)

school.pop("city")
print (school)

del school["country"]
print (school)

school.clear()
print (school)    #{} 

del school # deleted object




x = {"A" : 1, "B" : 2, "C" : 3}
x_keys = x.keys()

print(x_keys)

x_values = x.values()
print(x_values)

x_items = x.items()
print(x_items)
'''
dict_keys(['A', 'B', 'C'])
dict_values([1, 2, 3])
dict_items([('A', 1), ('B', 2), ('C', 3)])
'''

x["D"] = 4
print(x_keys)
print(x_values)
print(x_items)
'''
dict_keys(['A', 'B', 'C', 'D'])
dict_values([1, 2, 3, 4])
dict_items([('A', 1), ('B', 2), ('C', 3), ('D', 4)])
'''

for value in x.values():
	print(value)
	
for key, value in x.items():
	print(key, value)

if "D" in x:
	print ("D is in x")
else:
	print("D is not in x")


#*****************

math_class = {
	"cours" : "calculus",
	"teacher" : {
		"name" : "John Nash"
	}
}
# a copy stil referencie at the same object
#is needed a deep copy function by import copy
print(math_class["teacher"]["name"])

math_copy = math_class.copy()

math_copy["teacher"]["name"] = "Luis Fil"
print(math_class)


math_copy_deep = copy.deepcopy(math_class)
math_copy_deep["teacher"]["name"] = ["Kultur Place"]
print("math_class: ", math_class)
print("math_copy_deep: ", math_copy_deep)


m = {"X" : 1, "Y" : 2}
n = {"Y" : 2 , "X" : 1}
print("m: ", m)
print("n: ", n)
if m == n:
	print("m == n")
