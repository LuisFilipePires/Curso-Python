
#returns a new string

my_str = "ABC"

new_str = my_str.zfill(8)

#          00000ABC
#my_str = "ABC"

print(new_str)

my_str = "-ABC"

new_str = my_str.zfill(8)
print(new_str)

my_str = "+ABC"
new_str = my_str.zfill(8)
print(new_str)

"""
output:
00000ABC
-0000ABC
+0000ABC

"""
