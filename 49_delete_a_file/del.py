
import os
'''
try:
	os.remove("text.txt")
except:
	print("file already delected")
   
rep = input("Do you want to create the file?\n",("*" * 8),"yes/no")
	#if (rep == "yes")
'''
if(os.path.exists("text.txt")):
	os.remove("text.txt")
else:
	print("File does not exist")

