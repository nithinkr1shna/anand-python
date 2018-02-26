#!/usr/bin/python
#now we are using inheritance to set up a ami balance account

class BankAccount:
	def __init__(self):
		self.balance =0

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

class MinBalanceAccount(BankAccount):

	def __init__(self, minbal):
		BankAccount.__init__(self)
		self.min_bal = minbal

	def withdraw(self, amount):
		if self.balance - amount < self.min_bal:
			return  "sorry min balance must be maintained"
		else:
			return BankAccount.withdraw(self , amount)


acc1 = MinBalanceAccount(100)
print acc1.deposit(500)
print acc1.withdraw(450)
print acc1.withdraw(100)