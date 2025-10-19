

str = "A miss is as good as a mile"
tuple = str.partition("as")

print(tuple)

tuple_not = str.partition("nothingthere")
print(tuple_not)


#rpartition brings the last occurance

tuple3 = str.rpartition("as")
print(tuple3)

"""
output:
('A miss is ', 'as', ' good as a mile')
('A miss is as good as a mile', '', '')
('A miss is as good ', 'as', ' a mile')


"""
