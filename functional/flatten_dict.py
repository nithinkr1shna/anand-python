#!/usr/bin/python

#program to flatten a rnested dict

def flatten_dict(string, dictionary, flattened):
	for key, value in dictionary.iteritems():
		if not isinstance(value, dict):
			if len(string) > 0:
				flattened[string+"."+key] = value
			else:
				flattened[string+ key] = value
		else:
			flatten_dict(key, value, flattened)

	return flattened

def flatten_dictionary(dictionary, flattened):
	return flatten_dict("",dictionary, flattened)

if __name__ == "__main__":
	d = dict()
	print flatten_dictionary({'a': 1, 'c': 7, 'b': {'y': 5, 'x': 4}},d)
	print flatten_dictionary({'a': 1, 'c': 7, 'b': {'y': 5, 'x': 4}, "f":8, "g":{"t":4, "k":{"i":1, "p":3}}},d)