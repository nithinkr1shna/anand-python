#!/usr/bin/python

#using iterator protocol to create a ryrange, which returns the raneg in reverse order


class yrange_rev:
	def __init__(self, start, end):
		self.start= start
		self.end = end

	def __iter__(self):
		self.res = 0
		self.final = self.end
		return self

	def next(self):
		if self.res < self.final:
			res =self.end
	
			self.end -=1
			self.res +=1
			return res
		else:
			raise StopIteration()


if __name__ == "__main__":
	for i in yrange_rev(1,10):
		print i

