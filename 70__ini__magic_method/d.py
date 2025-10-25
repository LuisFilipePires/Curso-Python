
'''
string1 = "42"

nbr = int(string1)

print(nbr + 1 )
'''

class Account:
	def __init__(self, balance):
		self.balance = balance
	def __int__(self):
		return(self.balance)


account1 = Account(1000)

print (int(account1.balance))
