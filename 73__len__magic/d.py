


print(len([1,2,3]))  # 3

class Orders:
	def __init__(self, items):
		self.items = items
	 
	def __len__(self):
		return(len(self.items))
#	def __bool__(self)  # it uses len to determinate true or false


order = Orders(["Pizza", "pasta", "Salade"])  #True

order_length = len(order)
print("Length: ", len(order))

order2 = Orders([])  #False

if(order):
	print("True")
else:
	print ("False")


if(order2):
	print("True")
else:
	print ("False")    #False
