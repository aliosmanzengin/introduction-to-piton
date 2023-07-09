nested1 = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]
y = nested1[1]
print(y)
print(y[0])

print([10, 20, 30][1])
print(nested1[1][0])

# The complex items in a list do not have to be lists. They can be tuples or dictionaries. The items in a list do not
# all have to be the same type, but you will drive yourself crazy if you have lists of objects of varying types. Save
# yourself some headaches and don’t do that.
nested2 = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"}]

# write code to print the value associated with key 'c' in the second dictionary (90)
print(nested2[1]['c'])
# write code to print the value associated with key 'b' in the third dictionary
print(nested2[2]['b'])
# add a fourth dictionary add the end of the list; print something to check your work.
nested2.append({"fourth dict": 4})
print(nested2[3])
# change the value associated with 'c' in the third dictionary from "yes" to "no"; print something to check your work
nested2[2]['c'] = 'no'
print(nested2[2]['c'])


# You can even have a list of functions (!).
def square(x):
    return x * x


L = [square, abs, lambda x: x + 1]

print("****names****")
for f in L:
    print(f)

print("****call each of them****")
for f in L:
    print(f(-2))

print("****just the first one in the list****")
print(L[0])
print(L[0](3))



info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }
color = info['personal_data']['physical_features']['color']
print (info['personal_data']['physical_features'])
info['personal_data']['physical_features'][5] = 999
print (info['personal_data']['physical_features'])
