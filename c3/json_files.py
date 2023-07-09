# json.loads() takes a string as input and produces a python object (a dictionary or a list) as output.
#
# Consider, for example, some data that we might get from Apple’s iTunes, in the JSON format:

import json

a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", ' \
           '"collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2': {'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}
print(json.dumps(sports, indent=2))