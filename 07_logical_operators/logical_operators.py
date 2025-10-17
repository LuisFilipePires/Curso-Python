
name = "Bob"
password = "1234"

#if statment Ture False
if (name == "Bob"):
	if(password == "1234"):
		print("Logged in")


if (name == "Bob" and password == "1234"):
	print("Logged In")
	
print("True and True: ", True and True)
print("True and False: ", True and False)
print("False and True: ", False and True)
print("False and False: ", False and False)

print("True or True: ", True or True)
print("True or False: ", True or False)
print("False or True: ", False or True)
print("False or False: ", False or False)


print("not True: ", not True)
print ("not False: ", not False)

#can't divide by Zero
#ZeroDivisionError: division by zero
#print ( (40/0 == 0) or True)
print("True or (40/0 == 0): ", True or (40/0 == 0))  #problem, the first operator

print ("not False or True: ", not False or True)
#the order of operators defines
# not
# and
# or

