#!/usr/bin/python

# recursion , finding exponent 
#in recursion there will be a terminating condition


def exp(x, n):

	if n == 0:
		return 1
	else:
		return x *exp(x, n-1)


print exp(2, 4)