


empty_list = bool([])
print(empty_list)   # False


class Order:
	def __init__(self, items):
		self.__items = items
		'''
	def __len__(self, len):
		return (len(self.__items))
		'''
	def __bool__(self):
		if(len(self.__items) == 0):
			return False
		else:
			return True


#if theres no __bool__ method defined
#but a __len__ is defined the length will be used
#like boolean		
		
		
	
order = Order(["Pizza", "Pasta", "Salad"])

#by default its True
order_bool = bool(order)
		
print(order_bool)  #True
