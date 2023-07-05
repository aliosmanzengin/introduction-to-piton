dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_keys = sorted(dictionary)
print(sorted_keys)

"""Here things get a little confusing because we have two different meaning of the word “key”. One meaning is a key
in a dictionary. The other meaning is the parameter name for the function that you pass into the sorted function.

Remember that the key function always takes as input one item from the sequence and returns a property of the item.
In our case, the items to be sorted are the dictionary’s keys, so each item is one key from the dictionary. To remind
ourselves of that, we’ve named the parameter in tha lambda expression k. The property of key k that is supposed to be
returned is its associated value in the dictionary.
Hence, we have the lambda expression -----> lambda k: d[k]."""

"""
NOTE
When we sort the keys, passing a function with key=lambda x: d[x] does not specify to sort the keys of a dictionary. 
The lists of keys are passed as the first parameter value in the invocation of sort. The key parameter provides a 
function that says how to sort them."""

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
"""        
y =(sorted(d.keys(), key=g, reverse=True))

# now loop through the keys
for k in y:
    print("{} appears {} times".format(k, d[k]))
"""
# now loop through the sorted keys
for k in sorted(d, key=lambda k: d[k],
                reverse=True):  # when passing dictionary as variable, just giving the dictionary name will enough to
    # look for dictionary keys
    print("{} appears {} times".format(k, d[k]))

print("\n===================================================================================\n")
# Example
L = [4, 5, 1, 0, 3, 8, 8, 2, 1, 0, 3, 3, 4, 3]

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1


def g(k, d):
    return d[k]


ks = d.keys()
print(sorted(ks, key=lambda x: g(x, d)))
print(sorted(ks, key=lambda x: d[x]))

print("\n===================================================================================\n")
# example
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values = sorted(dictionary, reverse=True, key=lambda x: dictionary[x])
print(sorted_values)

# In the code below, we are going to sort a list of fruit words first by their length, smallest to largest,
# and then alphabetically to break ties among words of the same length. To do that, we have the key function return a
# tuple whose first element is the length of the fruit’s name, and second element is the fruit name itself.
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)  # kiwi
    # pear
    # apple
    # mango
    # peach
    # papaya
    # blueberry

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)
for fruit in new_order:
    print(fruit)  # blueberry
    # papaya
    # peach
    # mango
    # apple
    # pear
    # kiwi
# Not only does it sort the words from largest to smallest, but also in reverse alphabetical order!

# One solution is to add a negative sign in front of len(fruit_name), which will convert all positive numbers to
# negative, and all negative numbers to positive. As a result, the longest elements would be first and the shortest
# elements would be last.
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)

# When to use a Lambda Expression

# we want to sort the states in order by the length of the first city name. Here, it’s pretty easy to compute that
# property. states[state] is the list of cities associated with a particular state. So If state is a list of city
# strings, len(states[state][0]) is the length of the first city name. Thus, we can use a lambda expression:
states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: len(states[state][0])))


# For our second sort order, the property we want to sort by is the number of cities that begin with the letter ‘S’.
# The function defining this property is harder to express, requiring a filter and count accumulation pattern. So we
# are better off defining a separate, named function.
def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct


states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))
