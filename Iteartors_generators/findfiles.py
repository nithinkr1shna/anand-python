#!/usr/bin/python

#finds all files in a particular directory
#the program finds the directory 


import os
import sys

def find_dir(desired_directory):
	for root, dirs, files in os.walk(os.getcwd()):
		for dir in dirs:
			if dir == desired_directory:
				return os.listdir(os.path.join(root,dir))



for files in find_dir(sys.argv[1]):
	print files
