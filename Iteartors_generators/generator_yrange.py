#!/usr/bin/python

#use of generators instead on iterators

def yrange(start, end):
	while start <= end:
		yield start
		start += 1



if __name__ == "__main__":
	for i in yrange(1, 10):
		print i