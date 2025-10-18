# The center() method returns a new string.
# It centers the text within a field of a given width,
# padding it with spaces by default.


string = "text"

new_string = string.center(10)
print (new_string)

print("old: ", len(string))
print("new: ", len(new_string))

other_string = string.center(15, "-")
print (other_string)

"""
output:
   text   
old:  4
new:  10
------text-----
'''
