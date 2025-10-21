
add_one = lambda x: x + 1
print(add_one(5))     #6

add_1 = lambda : 10
print(add_1())  #10

multiply = lambda x, y : x * y
print(multiply(12,3))  # 36

print((lambda x,y : x * y)(20,50))   #1000

#***********************************************

numbers = [1,2,3,4,5,6,7,8]

def doubler(x):
	return x * 2

doubled = map(doubler, numbers)
print(list(doubled))

#use lambda insted
doubled2 = map(lambda x : x * 2 , numbers)
print(list(doubled2))

'''
output
6
10
36
1000
[2, 4, 6, 8, 10, 12, 14, 16]
[2, 4, 6, 8, 10, 12, 14, 16]

'''
