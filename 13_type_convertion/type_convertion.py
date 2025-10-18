 #type casting 

"""
Implicit → Python converts automatically when safe.

Explicit → You convert manually using int(), float(), str(), etc.
"""

#implicit conversion
x = 2
y = 3.5

print ("x: ", x)
print("type x: ", type(x))
print("y: ", y)
print("type y: ", type(y))

z = x + y
print("z = x + y")
print("type z:", type (z))

#explicit conversion

ai = 2
print("type ai: ", type(ai))

af = float(ai)
print("af = float(ai) ", af)
print("type af: ", type(af))

b = "2.45"
print("b: ", b)
print("type(b): ", type(b))

b = float(b)
print("b = float(b) ", b)
print("type(b): ", type(b))


#xs = "5.25" #convert string (float) directly to int ->Error
xs = 5
print ("xs: ", xs)
print ("type (xs): ", type(xs))
 
xi1 = int(xs)
print("xi1: ", xi1)
"""
 in <module>
    xi1 = int(xs)
          ^^^^^^^
ValueError: invalid literal for int() with base 10: '5.25'
"""

xf = 7.33
print("xf: ", xf)
print("type(xf): ", type(xf))
xf1 = int (xf)
print("xf1 = int(xf)", xf1)
print("type(xf1): ", type(xf1))

y1 = 7
print("y1: ", y1)
print("type(y1): ", type(y1))
y2 = str(y1)
print("y2: ", y2)
print("type(y2): ", type(y2))

y3 = 7.342
print("y3: ", y3)
print("type(y3): ", type(y3))
y4 = str(y3)
print("y4 = str(y3): ", y4)
print("type(y4): ", type (y4))


slist = str([1, 2, 3])
print("slist: ", slist)
print("type(slist): ", type(slist))



