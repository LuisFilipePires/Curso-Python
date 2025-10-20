

#start stop step
range(0, 5, 1)
print(list(range(0, 5, 1)))  #[0, 1, 2, 3, 4]


print(list(range(3, -8, -2))) # [3, 1, -1, -3, -5, -7]

print(list(range(4,9))) # [4, 5, 6, 7, 8]

print(list(range(6))) # [0, 1, 2, 3, 4, 5]


range1 = range(0, 10, 6)
range2 = range(0, 11, 6)
print(list(range1))
print(list(range2))
if range1 == range2 : print("range1 equals rang2")
'''\[0, 6]
[0, 6]
range1 equals rang2
'''

#
mylist= [2,4,6,8,10,12,14,16,18,20]
myrange = range(2,22,2) # with 3 numbers print a bi sequency
print(list(myrange)) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print("myrane.start: ", myrange.start)
print("myrange.stop: ", myrange.stop)
print("myrange.step: ", myrange.step)
'''output:
myrane.start:  2
myrange.stop:  22
myrange.step:  2
'''

#examples
#run a loop body x10
for i in range(10):
	print(i)
	
print("*" *12)

#print counter from 3 to 30 step by 5

for i in range(3, 30, 5):
	print(i)
#

# +  - no concatenation
# *  - no repetition

if (1 in range(0, 4)) : print("1 is in the range")
if (10 not in range(0, 4)) : print("10 is not in the range")

print("len: ", len(range(0, 4)))
print("min: ", min(range(0, 4)))
print ("max: ", max(range(0, 4)))

#count how many 
print("count nbr 1: ", range(0, 20).count(1))

#index of
#value 2345
#index 0123
print("4 is in index: ", range(2,6).index(4))
#print the index of
print(range(2, 6)[1]) #3

#slicing
print(list(range(2, 20, 2)[2:10:3]))
#[6, 12, 18]


