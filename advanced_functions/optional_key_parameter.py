"""
!!!Note
It is a little confusing that we are reusing the word key so many times. The name of the optional parameter is key.
We will usually pass a parameter value using the keyword parameter passing mechanism. When we write key=some_function
in the function invocation, the word key is there because it is the name of the parameter, specified in the
definition of the sort function, not because we are using keyword-based parameter passing.


"""

L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute)
print(L2)

#or in reverse order
print(sorted(L1, reverse=True, key=absolute))
