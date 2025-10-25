


class Data:
	def __init__(self, value):
		self.value = value
	def __float__(self):
		return (self.value)


data = Data(44.5)

#problem with a object copy constructor
new_data = float(data)
#or
new_data2 = data.value

print(float(data.value))
print(type(new_data))
	
