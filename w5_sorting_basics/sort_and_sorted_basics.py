L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2)  # unchanged

print("----")

L2.sort()
print(L2)
print(L2.sort())  # return value is None

print(sorted("Dumla dumla da"))

# Optional reverse parameter
L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))

L1 = [1, 7, 4, -2, 3]


def absolute(x):
    print("--- figuring out what to write on the post-it note for " + str(x))
    if x >= 0:
        return x
    else:
        return -x


print(absolute(3))
print(absolute(-119))
# we can pass the absolute function to sorted in order to specify that we want the items sorted in order of their
# absolute value, rather than in order of their actual value.
print("About to call sorted")
L2 = sorted(L1, key=absolute)
print("Finished execution of sorted")
print(L2)

# When we pass that function object, it is not automatically invoked. Instead, it is just bound to the formal
# parameter key of the function sorted.
print(sorted(L1, reverse=True, key=absolute))
# What the sorted function does is call that key function once for each item in the list that’s getting sorted. It
# associates the result returned by that function (the absolute function in our case) with the original value. Think
# of those associated values as being little post-it notes that decorate the original values. The value 4 has a
# post-it note that says 4 on it, but the value -2 has a post-it note that says 2 on it. Then the sorted function
# rearranges the original items in order of the values written on their associated post-it notes.

"""
NOTE
It is a little confusing that we are reusing the word key so many times. The name of the optional parameter is key. 
We will usually pass a parameter value using the keyword parameter passing mechanism. When we write key=some_function 
in the function invocation, the word key is there because it is the name of the parameter, specified in the 
definition of the sort function, not because we are using keyword-based parameter passing."""

"""EXAMPLE QUESTION You will be sorting the following list by each element’s second letter, a to z. Create a function 
to use when sorting, called second_let. It will take a string as input and return the second letter of that string. 
Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. Do not use 
lambda."""
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']


def second_let(s):
    return s[1]


sorted_by_second_let = sorted(ex_lst, key=second_let)
print(sorted_by_second_let)

# ------------------
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']


def last_char(s):
    return s[-1]


nums_sorted = sorted(nums, reverse=True, key=last_char)

# using sorted with key LAMBDA function
# sort the list nums based on the last digit of each number from highest to
# lowest. However, now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda = sorted(nums, reverse=True, key=lambda x: x[-1])


# Create a function called last_four that takes in a single ID number and returns the last four digits. For example,
# the number 17573005 should return 3005. Then, use the resulting function to sort the list of ids stored in the
# variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids
def last_four(x):
    print(x)
    print(str(x)[-4:])
    return str(x)[-4:]


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids = sorted(ids, key=last_four)
sorted_id = sorted(ids, key=lambda x: str(x)[-4:])  # with lambda
