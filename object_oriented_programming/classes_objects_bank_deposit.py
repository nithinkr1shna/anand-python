#!/usr/bin/python
#now we are using classes and objects to acheive the same in a elegant way

class BankAccount:

	def __init__(self):
		self.balance = 0
		self.min_bal = 100

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		if amount > self.balance:
			return "insufficient funds"
		elif self.balance - amount < self.min_bal:
			return "you've to keep min balance: 100\ncurrent balance is: {} \nCan't withdraw {}".format(self.balance, amount)
		else:
			self.balance -= amount
			return self.balance

acc1 = BankAccount()
print acc1.deposit(200)
acc2 = BankAccount()
print acc2.deposit(500)

print acc1.withdraw(150)
print acc2.withdraw(650)
