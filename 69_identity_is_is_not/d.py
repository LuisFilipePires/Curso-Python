

 
#knows if 2 variables are not reference the same object in memory

list1 = [1,2,3]
list2 = [1,2,3]
list3 = list2
 
 
print("id1: ", id(list1))
print("id2: ", id(list2))
print("id3: ", id(list3))


#if two objects are referencing the same memory location

if list2 is list3:
	print("List2 is List3")
	
#check list1 list2, id

if list1 is list2:           #list1 is NOT list2
	print("list1 is list2")
else:
	print("list1 is NOT list2")
	
if list1 == list2:           #if the value is the same
	print("list1 equals list2")
	
	
	
#both are not referencing the same object
if list1 is not list2:
	print("list1 is not list2")
