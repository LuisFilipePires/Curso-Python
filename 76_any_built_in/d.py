

print(any([False, True, False]))   # True
print(any([False, False, False]))  # False
print(any([False, "", False]))   # empty string  False


print(any({0,1}))   # True
print(any({0}))     # False

#check if any the keys are True
print(any({0:True, 1:False}))   # True  ,key 0: is evaluated as False, 1 evaluated as True
print(any({0:True}))     # False
print(any({0:False, 1:False})) #True

strings = (["apple", "against", "application"])
print ([s.startswith("aga") for s in strings])	  #[False, True, False]


if (any([s.startswith("aga") for s in strings])):
	print ("a string does begin with 'aga'")   #True
else:
	print ("no  string begins with 'aga'")
