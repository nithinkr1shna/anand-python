#!/usr/bin/python

#unflatten a flattened list
# {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}

def unflatten_dict(dictionary, unflattened):
	for key, value in dictionary.iteritems():
		if len(key) > 1:
			new_key = key.split(".")
			if new_key[0] not in unflattened: 
				unflattened[new_key[0]] = {new_key[1]: value}
			else:
				existing = unflattened[new_key[0]]
				existing.update({new_key[1]: value})
				unflattened[new_key[0]] = existing
		else:
			unflattened[key] = value

	return unflattened



if __name__ == "__main__":
	print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}, dict())