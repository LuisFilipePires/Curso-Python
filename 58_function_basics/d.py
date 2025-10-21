


def greetings(person_name = "John"):
	print("Hi", person_name)
	print("How are you feeling?")
	feelings = input("Feeling 	")
	return feelings

'''
greetings("Filipe")
greetings("Omar") 
greetings()
'''
filipe_feeling = greetings("Filipe")
print("Filipe is feeling ", filipe_feeling)



def operations(x, y):
	return x + y, x - y, x* y


a = 5
summ, dif, product = operations(a, 2)
print("sum: ", summ)
print ("dif: ", dif)
print("product: ", product)

def output(x1, x2, x3):
	print("x3: ", x3)

output("no" , "no", "yes")
#use keywords as parameter
output(x3 = "yes", x1 = "no", x2 = "not")



#ummutable int in function

def modify(x):
	x = x + 1
	print ("x: ", x)

x = 10
modify(x)
print ("x: ", x)

#muttable items in function

def modify_list(l):
	l.append(34)

l = [1,2,3]
modify_list(l)
print("l: ", l)

"""
output:
Hi Filipe
How are you feeling?
Feeling 	good
Filipe is feeling  good
sum:  7
dif:  3
product:  10
x3:  yes
x3:  yes
x:  11
x:  10
l:  [1, 2, 3, 34]

"""


