#suppose we want to model a bank account with the suppot for deposit and withdraw ops. 
#one way of doing it is with the help of a gobal state/variable

#ex:

balance= 0

def deposit(amount):
	global balance
	balance += amount
	return balance

def withdraw(amount):
	global balance
	balance -= amount
	return balance


print "New balance:", deposit(100)
print "New balance:", withdraw(50)

#but in the case of multiplr bank acounts this wont work well, we need to use objects and classes