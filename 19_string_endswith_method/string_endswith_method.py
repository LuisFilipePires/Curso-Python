my_string = "Carol Shaw"

print(my_string.endswith("Shaw"))
#output: True

print(my_string.endswith("Carol"))
#output: False

print(my_string.endswith("Carol Shaw"))
#output: True because that string ends with the same end

print(my_string.endswith("Harnold Clever Shaw"))
#output: False -> compares the 2d string with the first strings ending

#0123456789
#Carol Shaw

#but we can compare by index (between index +1
print(my_string.endswith("Sh",6,8 ))  #compares "h"
#output: True

print(my_string.endswith("h",6,8 ))  #compares "h"
#output:True

print(my_string.endswith(("Shaw", "Smith" )))
#output:True
my_string = "Carol Smith"
#output:True
print(my_string.endswith(("Shaw", "Smith" )))
#output:True



