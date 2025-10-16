
print(4)
print(2.5)
print("text")
print (False)

print ("text 1", "text2", "text3")

name = "ally"
age = 20
print ("First name:", name, ", Age:", age)
# separeted spaces
print (1,2,3,4,5,6,7)
print (1,2,3,4,5,6,7, sep=",")

#testing new line in print()
print("This is a line")
print("This is another line")

print("On the ", end=" ")
print("same line")

text_file = open("file.txt", "w")

print(1,2,3,4,5,6,7, file=text_file)
text_file.close()

#if end is changed, the output will stay in a buffer
import time

print("output x", end=", ") # stay in the buffer
time.sleep (5)              # 5 seconds pause to observe buffering
print("then y!")            # flushes the buffer and prints everything

#now if we want to force the first print t fush
print("output x", end=", ", flush=True) # force print to flush
time.sleep (5)              # 5 seconds pause to observe buffering
print("then y!")            # prints the last one