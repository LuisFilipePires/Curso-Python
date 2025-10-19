
#find return an index,    -1 if error



#       0123456789........
text = "To be or not to be"

index = text.find("be")
print(index) 

#find occurence from index 4
index = text.find("o", 4)
print(index)

index = text.find("be", 2,5)
print(index) 

print("*******")
#index
index = text.index("o", 4, 9)
print(index)

print("rfind, rindex")
index = text.rfind("be")
print(index) 

index = text.rindex("be")
print(index) 
