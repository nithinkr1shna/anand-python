#!/usr/bin/python

#tree map
#input :
''' 
>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]

'''

def treemap(f, nested_list):
	res = list()
	for each in nested_list:
		if isinstance(each, list):
			res.append(treemap(f, each))
		else:
			res.append(f(each))

	return res
	


if __name__ == "__main__":
	print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])

