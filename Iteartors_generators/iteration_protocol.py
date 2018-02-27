#!/usr/bin/python

#the iteration protocol is both the __iter__ next methods

# we have a function called iter , it takes an iterable object and retuns an iterator

#ex:
# x = iter([1,2,3])
# x.next()
#>>1
#x.next()
#>>2
#x.next()
#>>3
#x.next()
#trace back ! raises stop Iteration

#iterators are implemented as classes

#example yrange iterator

class yrange:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __iter__(self):
		return self

	def next(self):
		if self.start <= self.end:
			result = self.start
			self.start += 1
			return result
		else:
			raise StopIteration()


if __name__ == "__main__":
	for i in yrange(1, 100):
		print i