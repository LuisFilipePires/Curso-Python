


str1 = "Good"
str2 = "morning"
str3 = " to you!"

concat = str1 + " " +str2
print(concat)

concat += str3
print(concat)

#cant concatenat different types
speed = 20
units = " kl/h"

speedout = str(speed) + units
print(speedout)
#*****************************

name_list = ["kam", "Evien", "Suzan"]
names_output = ", ".join(name_list)
print(names_output)

#format {}
s1 = "Good"
s2 = "Evening"

#"{} {}"
s_out = "{} {}".format(s1, s2)
print(s_out)

#"%s %s"
s_out2 = "%s %s" % (s1, s2)
print(s_out2)


#f{} {}
s_out3 = f"{s1} {s2}"
print(s_out3)






