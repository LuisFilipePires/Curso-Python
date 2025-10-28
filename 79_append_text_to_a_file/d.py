

#how to run
#more text.txt   -> display text

filename = input("File: ")
text = input("text: ")

with open(filename, "a") as file:
	file.write(text)
