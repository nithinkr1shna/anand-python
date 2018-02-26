#!/usr/bin/python
# we are using dictionary in python to acheive the idea of multiple bank accounts
# here we use local state balance for each accounts

def make_account():
	return {'balance': 0}

def deposit(account, amount):
	account['balance'] += amount
	return account['balance']

def withdraw(account, amount):
	account['balance'] -= amount
	return account['balance']


acc1 = make_account()
print deposit(acc1, 100)
acc2 = make_account()
print deposit(acc2, 200)

print withdraw(acc1, 50)
print withdraw(acc2, 100)
