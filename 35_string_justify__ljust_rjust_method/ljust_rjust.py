#spaces by default
#ljust / rjust  / center (>number<) total of characters

string = "text"

right_justified = string.rjust(10, "*")
print (right_justified)

left_justified = string.ljust(10, "*")
print(left_justified)

center_justified = string.center(10, "+")
print(center_justified)


"""
output:
******text
text******
+++text+++
"""
