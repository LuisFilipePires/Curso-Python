
# Checks if each word starts with an uppercase letter
# and all remaining letters in each word are lowercase.
#ignore digits and :

my_str = "The Social Network"
print(my_str.istitle())
#output: True

my_str = "The Social NetWork"
print(my_str.istitle())
#output: False



