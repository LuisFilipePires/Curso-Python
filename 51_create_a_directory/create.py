import os

#os.mkdir("new directory")


#pwd /home/fil/Documents/Python_course/51_create_a_directory
try:
	os.mkdir ("/home/fil/Documents/Python_course/51_create_a_directory/new directory2")
except:
	print("make dir fail")


#FileExistsError: [Errno 17] File exists: 'new directory'
#exception
