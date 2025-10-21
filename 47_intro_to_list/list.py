
#index	 0   1  2
a = 	[2, -4, 6]
print(a)

#by index
print(a[0])
print(a[2])

#modify
a[0] = 200
print(a)

#increment a new iten
a.append(7)
print(a)

#insert item 3 at index 1
a.insert(1,3)
print(a)

#extend the list
a.extend([8, 55,71])
print(a)

#delete itens at index
del a[1]
print(a)

#remove specific number
a.remove(8)
print(a)


#remove the las with pop
last = a.pop()
print(a)
print (last)

#remove pop index
third = a.pop(2)
print(a)
print(third)

#print length
print("length: ", len(a))

#verify item
if (200 in a):
	print("200 is in list")
else:
	print("200 is not in List")
	
#reverse itens
a.reverse()
print(a)

#sort list
a.sort()
print(a)

#sort in descend order
a.sort(reverse = True)
print (a)

#string List
print("*" * 25)
str_list = ["luke", "Matilda", "Louis", "Anton"]
print(str_list)

#sort
str_list.sort()
print(str_list)


#mixed list
mix_list = [2, True, "Grace", "x", [1,2]]
print(mix_list)
for item in mix_list:
	print(item,"*" * 8, type(item))

x = [1, 2,3]
y = x

#reference
#         [1, 2  , 3]
#           /     \
#        x          y
# x and y reference to the same list
y[1] = 230
print("x: ", x)
print ("y: ", y)

#copy
q = [1, 2, 3]
w = q.copy()

w[1] = 222
print("q: ", q)
print("w: ", w)


#slice returns a new objet (list)
#           0   1   2   3   4   5
letters = ["a","b","c","d","e","f"]
letters_slice = letters[1:4] # >=1 and < 4
print(letters_slice)

for letter in letters:
	print(letter)

print("clear", "*" * 10)
letters.clear()
print (letters)


#concatenate
list1 = [1,2,3]
list2 = [4,5,6]
new_list = list1 + list2
print ("list1: ", list1)
print("list2: ", list2)
print("new list: ", new_list)
