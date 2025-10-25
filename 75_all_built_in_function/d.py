

#all([True, True,True])

print (all([True, True,True]))  #True

print (all([True, True,False]))  # False
print (all([True, True,""]))     #False
print (all([True, True,[1,2,3]])) #True

#but if the list is empty , it returns True
print (all([]))   #True 

#with a set
print (all({1,2,3}))   #True
print (all({1,0,3}))   #False

#key {}
print (all({1:False, 2:False}))    #True
print (all({1:False, 0:False}))    #False 

strings = ["apple", "apply", "applications"]

print([s.startswith("appl") for s in strings])

if (all([s.startswith("appl") for s in strings])) :
	print("All the items begin with 'appl'")
else:
	print("All the items do not begin with 'appl'")
