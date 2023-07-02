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

print("\n*********************************************\n")

#  Dictionary methods

# The first technique involves iterating over the keys of the dictionary using the keys method. The keys method
# returns a collection of the keys in the dictionary.
inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}

for akey in inventory.keys():  # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())  # Make a list of all of the keys
print(ks)
print(ks[0])  # Display the first key

print("\n*********************************************\n")

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
    print("Got key", k)

print("\n*********************************************\n")

# The values method returns a collection of the values in the dictionary. Here’s an example that displays a list of
# the values:
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))

for v in inventory.values():
    print("Got", v)

print("\n*********************************************\n")
# The items method returns a collection of tuples containing each key and its associated value. Take a look at this
# example that iterates over the dictionary using the items method:
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.items()))
print(inventory.items())
print(type(inventory.items()))  # <class 'dict_items'>

for k, v in inventory.items():
    print("Got", k, "that maps to", v)

"""
Technically, keys(), values(), and items() don’t return actual lists. Like the range function , they return 
objects that produce the items one at a time, rather than producing and storing all of them 
in advance as a list. If you need to perform an operation on the result of one of these methods such as extracting 
the first item, you must convert the result to a list using the list conversion function. For example, if you want to 
get the first key, this won’t work: inventory.keys()[0]. You need to make the collection of keys into a real list 
before using [0] to index into it: list(inventory.keys())[0].
"""

"""Looking up a value in a dictionary is a potentially dangerous operation. When using the [] operator to access a 
key, if the key is not present, a runtime error occurs. There are two ways to deal with this problem.
"""
print("\n*********************************************\n")

# The first approach is to use the in and not in operators, which can test if a key is in the dictionary:

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

print(430 in inventory)  # false

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")

# The second approach is to use the get method. get retrieves the value associated with a key, similar to the []
# operator.
# The important difference is that get will not cause a runtime error if the key is not present. It will
# instead return the value None. There exists a variation of get that allows a second parameter that serves as an
# alternative return value in the case where the key is not present. This can be seen in the final example below. In
# this case, since “cherries” is not a key, get returns 0 (instead of None).
print("\n*********************************************\n")

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))
print("\n*********************************************\n")

# ALIASING AND COPYING
"""Because dictionaries are mutable, you need to be aware of aliasing (as we saw with lists). Whenever two variables 
refer to the same dictionary object, changes to one affect the other. For example, opposites is a dictionary that 
contains pairs of opposites."""


opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)  #True

alias['right'] = 'left'
print(opposites['right'])

#  As you can see from the is operator, alias and opposites refer to the same object.
#
# If you want to modify a dictionary and keep a copy of the original, use the dictionary copy method. Since acopy is
# a copy of the dictionary, changes to it will not effect the original.

opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
acopy = opposites.copy()
acopy['right'] = 'left'    # does not change opposites

print("\n*********************************************\n")
