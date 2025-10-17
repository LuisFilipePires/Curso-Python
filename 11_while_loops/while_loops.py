
i = 1

#while True
while i < 10:
	print (i)
	if i == 3:
		#break
		i += 3
		continue
	i+=1

print ("loop done")

#text loop

text = ""

while (text != "stop"):
	text = input("please enter stop\n")
	print("Bravo ", text) if text == "stop" else print(text)
