 

number = 1 + 2

print (number)

other = number
print(other)
#in python varoables are like boxes
#the value of number its not coppied to other
#it is a reference

list1 = [1,2,3]
list2 = list1
list2[0] = 10
print ("list1: ", list1)

#its possible to have a copy of variable

list01 = [10,20,30,40,50,60,70]
list02 = list01.copy()

list02[0] = 573

print("list01: ", list01)
print("list02: ", list02)

q = w = 100

print("q", q, "w", w, sep=": ")

q, w = 2, 8
print("q", q, "w", w, sep=": ")
q, w = w, q
print("q", q, "w", w, sep=": ")

number = 1
number += 2
print("number += 2", number, sep=": ")

number *= 10
print("number *= 10", number, sep=": ")
number **= 3
print("number **=3 ", number, sep=": ")
number = 10
number /= 3
print("number = 10, number /=3 ", number, sep=": ")

number = 10
number //= 3
print("number = 10, number //=3 ", number, sep=": ")

number = 10
number %= 3
print("number = 10, number %=3 ", number, sep=": ")

"""
output:
3
3
list1:  [10, 2, 3]
list01:  [10, 20, 30, 40, 50, 60, 70]
list02:  [573, 20, 30, 40, 50, 60, 70]
q: 100: w: 100
q: 2: w: 8
q: 8: w: 2
number += 2: 3
number *= 10: 30
number **=3 : 27000
number = 10, number /=3 : 3.3333333333333335
number = 10, number //=3 : 3
number = 10, number %=3 : 1
"""
