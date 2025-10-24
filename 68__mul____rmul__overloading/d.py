from numbers import Number

class Population:
	def __init__(self, initial_count):
		self.count = initial_count
	
	def __mul__(self, other):
		if (isinstance(other, Number)):
			return (Population(self.count * other))
		return Population(self.count * other.count)  # returns new object
	
	def __rmul__(self, other):
		return (Population(self.count * other))
		#a * b = b * a
		 
		 

population1 = Population(100)
population2 = Population(5.5)


new_population = population1 * population2 
print("new_population: ", new_population.count) 

#if (isinstance(other, int))

new_popul_2 = population1 * 15
print("new_popul: ", new_popul_2.count) 

new_pop3 = 6 * population2
print ("pop3: ", new_pop3.count)


