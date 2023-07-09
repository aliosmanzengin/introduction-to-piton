"""
 MAP
takes two arguments, a function and a sequence. The function is the mapper that transforms items. It is
automatically applied to each item in the sequence. You don’t have to initialize an accumulator or iterate with a for
loop at all.

"""
"""
NOTE
Technically, in a proper Python 3 interpreter, the map function produces an “iterator”, which is like a list but 
produces the items as they are needed. Most places in Python where you can use a list (e.g., in a for loop) you can 
use an “iterator” as if it was actually a list. So you probably won’t ever notice the difference. If you ever really 
need a list, you can explicitly turn the output of map into a list: list(map(...)). In the runestone environment, 
map actually returns a real list, but to make this code compatible with a full python environment, we always convert 
it to a list.
"""


def triple(value):
    return 3 * value


def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)


def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4 * value, a_list)
    return list(new_seq)


things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)

things = [2, 5, 9]

things4 = map((lambda value: 4 * value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5 * value), [1, 2, 3])))

# ==========================================================================================================
"""FILTER takes two arguments, a function and a sequence. The function takes one item and return True if the item 
should. It is automatically called for each item in the sequence. You don’t have to initialize an accumulator or 
iterate with a for loop."""


def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)


print(keep_evens([3, 4, 6, 7, 0, 1]))

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = list(filter(lambda v: 'w' in v, lst_check))
map_testing = list(map(lambda t: 'Fruit: ' + t, lst_check))

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
print(l2)
print("=============")
opposites = list(filter(lambda t: len(t[0])>3 and len(t[1])>3 ,zip(l1,l2)))
print(opposites)
