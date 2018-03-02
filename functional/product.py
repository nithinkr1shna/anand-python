#!/usr/bin/python

#find product of two nums using + and - recursively


def mul(x, y):
	if y == 0:
		return 0
	if y > 0: 
		return (x + mul(x, y-1))
	if y < 0:
		return -mul(x, -y)


if __name__ == "__main__":
	print mul(2,3)
	print mul(4,5)
	print mul(-5, 10)