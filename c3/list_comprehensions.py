"""Python provides an alternative way to do map and filter operations, called a list comprehension. Many programmers
find them easier to understand and write. List comprehensions are concise ways to create lists from other lists. The
general syntax is:
[<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]
where the if clause is optional. For example,"""
things = [2, 5, 9]

yourlist = [value * 2 for value in things]

print(yourlist)  # [4, 10, 18]


# difference from a regular for loop is that each time the expression is evaluated, the resulting value is appended
# to a list. That happens automatically, without the programmer explicitly initializing an empty list or appending
# each item.

# The if clause of a list comprehension can be used to do a filter operation. To perform a pure filter operation,
# the expression can be simply the variable that is bound to each item. For example, the following list comprehension
# will keep only the even numbers from the original list.

def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list


print(keep_evens([3, 4, 6, 7, 0, 1]))

# You can also combine map and filter operations by chaining them together, or with a single list comprehension.
things = [3, 4, 6, 7, 0, 1]
# chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x * 2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x * 2 for x in things if x % 2 == 0])


# Example
# The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension
# to accomplish the same thing. Assign it the the variable lst2. Only one line of code is needed.
L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

lst2 = [num for num in L if num > 10]


# Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the
# dictionary tester. Do this using a list comprehension.
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

compri = [names['name'] for names in tester['info']]
print(compri)

