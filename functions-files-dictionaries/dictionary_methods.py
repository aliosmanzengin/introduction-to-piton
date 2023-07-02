
eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos', 'age': 23}

eng2sp['four'] = 'quadro'

value = eng2sp['two']
print(value)
print(eng2sp['one'])
print(eng2sp)
eng2sp['age'] = eng2sp['age'] + 23
print(eng2sp)

print("number of key-value pairs", len(eng2sp))
del eng2sp['four']
print("number of key-value pairs", len(eng2sp))
print(eng2sp)


#  Dictionary methods

# The first technique involves iterating over the keys of the dictionary using the keys method. The keys method
# returns a collection of the keys in the dictionary.
inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())       # Make a list of all of the keys
print(ks)
print(ks[0])                      # Display the first key


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
    print("Got key", k)


# The values method returns a collection of the values in the dictionary. Here’s an example that displays a list of
# the values:
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))
print(list(inventory.items()))

for v in inventory.values():
    print("Got", v)


# The items method returns a collection of tuples containing each key and its associated value. Take a look at this
# example that iterates over the dictionary using the items method:
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.items()))

for k, v in inventory.items():
    print("Got", k, "that maps to", v)

