


countries = ["Luxembourg", "belgium", "Portugal", "Italy"]

for pais in countries:
	print(pais)

word = "Friends"

for charact in word:
	print(charact)

print("*" * 15)

for i in range(1, 11):
	print(i)

print("*" * 15)

for i in range(11):
	print(i,end=" ")

print("*" * 15)
print("while loop")
i  = 0
while(i <= 10):
	print(i, end=" ")
	i = i + 1
print("*" * 15)

print("range", ("*" * 10))
for i in range(2, 55, 5):
	print (i)
	
print ("*" * 15)

num = 5
for i in range(1,11,):
	print(num, " x ", i, " = ", i * num)

for num in range (1,11):
	for i in range(1,11,):
		print(num, " x ", i, " = ", i * num)
	print("*" * 20)
	
#continue
for i in range(1,11):
	if (i == 5):
		continue
	print(i)

#break
for letter in "Worlds":
	if letter == "r":
		print("found letter: ", letter)
		break
	print (letter, end = " ")

#pass
for i in range(1, 11):
	pass
