
import os

def create_files():
	try:
		f = open("./demofile.txt", "xt")
	except:
		print("File already exists")

	try:
		f = open("text.txt", "xt")
	except:
		print("File already exists")

	try:
		f = open("text2.txt", "xt")
	except:
		print("File already exists")

	try:
		f = open("./subdir/text.txt", "xt")
	except:
		print("File subdir already exists")

create_files()
path = "./"
print(os.listdir(path))

print(os.path.isfile("./text.txt"))
print(os.path.isfile("./subdir"))

for name in os.listdir(path):
	file = path + name
	if os.path.isfile(file):
		if(os.path.basename(file) == "del.py"):
			continue
		os.remove(file)
		
create_files()
