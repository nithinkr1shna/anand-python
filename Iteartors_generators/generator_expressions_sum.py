#!/usr/bin/python

def gen(l):
	a = (x * x for x in xrange(l))
	return a

print sum(gen(10))
