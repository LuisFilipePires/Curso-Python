
#  https://docs.python.org/3/library/stdtypes.html#str.splitlines

#return a newlist

text = "Line 1\nLine 2\nLine 3\nLine 4"

lines = text.splitlines() 
print(lines)

for line in lines:
	print(line)


#with end == true -> \n
lines = text.splitlines(True) 
print(lines)

#in empty text
text = ""
lines = text.splitlines() 
print(lines)
lines = text.splitlines(False) 
print(lines)

"""
output:
['Line 1', 'Line 2', 'Line 3', 'Line 4']
Line 1
Line 2
Line 3
Line 4
['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4']
[]
[]

"""
