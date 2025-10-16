a = 5
b = 2

print ("a = ", a)
print ("b = ", b)
print ("")

sum_result = a + b
print("a + b = ", sum_result)

#we can print the sum direct in print() function
print ("direct: a + b = ", a + b)
print ("a - b = ", a - b)
print ("a * b = ", a * b)

#power
print ("a ** b = ", a **b)
print ("a / b = ", a / b)
print ("a % b = ", a % b) #remainder modulo
print ("a // b = ", a // b) # floor division (divisao inteira) rounds down (2)
print ("a // -b = ", a // -b) #floor division calls the minus insignificant int (-3)

c = 4
d = 5
print("c before = ", c)
print ("d before = ", d)

c += d
print ("c now = ", c)

c = 4
c *= d
print ("c now = ", c)

result = 2 * 5 + 3
print ("result = ", result) # python using precedention

result = 2 * (5 + 3)
print ("result = ", result) # python using precedention