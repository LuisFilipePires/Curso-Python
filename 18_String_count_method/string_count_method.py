
string = "To be or not to be"

be_count = string.count("be")
print(be_count)

to_count = string.count("to") #lower case
print(to_count)

o_count = string.count("o")
print(o_count)

#            |        12
#          0123456789  |
#string = "To be or not to be"

o_range = string.count("o", 2,12)
print ("char \'o appears: ", o_range, " times")


"""
2
1
4
char 'o appears:  2
"""
