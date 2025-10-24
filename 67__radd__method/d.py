
from numbers import Number


class BankAccount:
	def __init__(self, initial_balance):
		self.balance = initial_balance

	def __add__(self, other):
		if(isinstance(other, Number)):
			total = self.balance + other
		else:
			total = self.balance + other.balance
		return (BankAccount(total))
	
	def __radd__(self, other):
		return (self.__add__(other))
		# a + b == b + a
	
	
	
account1 = BankAccount(1000)
account2 = BankAccount(2000)


#TypeError: unsupported operand type(s)
#for +: 'BankAccount' and 'BankAccount'
new_account = account1 + account2
	
print("new: ", new_account.balance)

new_account2 = account1 + 4000
print("new 2", new_account2.balance)


new_account3 = 5000 + account1
print("new 2", new_account3.balance)

new_account4 = 4600.500 + account1
print("new 2", new_account4.balance)
