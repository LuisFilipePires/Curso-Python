

# y = 1 + (x = 1)  # error

y = 1 + ( x := 1)

print ("y = ", y)
print("x = ", x)


(z := 5)
print("Z: ", z)

data = []
while (number := int(input("Enter a number (-1 to quit:)"))) != -1:
	data.append(number)
	
print(data)
