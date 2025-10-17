
age = 11
 
#True or False
if (age < 18):
	print("user is a child")
	print("user cannot vote")
elif(age >= 100):
	print("User is over 100!")
elif(age >= 65):
	print ("User is a senior")
	print("User can vote")
else:
	print("User is an adult")
	print("User can vote")
	
print ("If done!")

if age >= 18 and age <= 65 :
	print("user valid to vote")
	
#expression sentence in the same line

print("A") if age >= 18 else print("C")

adult = True if age >= 18 else False
print(adult)



	
