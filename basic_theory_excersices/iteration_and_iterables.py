"""
Create your own implementation of range(n): returns generator that generates integers from 0 to n(n>0). (Please use yield operator)

for i in my_range(3):
    print(i)
    0
    1
    2
    3
"""


# Implementing a custom range function using a generator and the 'yield' operator
def my_range(n):
    i = 0
    while i <= n:
        yield i
        i += 1


# Testing the function
for i in my_range(3):
    print(i)
