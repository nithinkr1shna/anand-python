#!/usr/bin/python

#read multiple files , return lines with length greater than 40
import sys

def readfile(filenames):
	for file in filenames:
		for line in open(file):
			if len(line) > 40:
				yield line



for line in readfile(sys.argv):
	print line