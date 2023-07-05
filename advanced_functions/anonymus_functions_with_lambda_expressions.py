# The syntax of a lambda expression is the word “lambda” followed by parameter names, separated by commas but not
# inside (parentheses), followed by a colon and then an expression. lambda arguments: expression yields a function
# object. This unnamed object behaves just like the function object constructed below.

def f(x):
    return x - 1


print(f)  # <function f>
print(type(f))  # <class 'function'>
print(f(3))  # 2

print(lambda x: x-2)  # <function <lambda>>
print(type(lambda x: x-2))  # <class 'function>
print((lambda x: x-2)(6))  # 4

# Note the paralells between the two. At line 11, f is bound to a function object. Its printed representation is
# “<function f>”. At line 13, the lambda expression produces a function object. Because it is unnamed (anonymous),
# its printed representation doesn’t include a name for it, “<function <lambda>>”. Both are of type ‘function’.

# A function, whether named or anonymous, can be called by placing parentheses () after it. In this case,
# because there is one parameter, there is one value in parentheses. This works the same way for the named function
# and the anonymous function produced by the lambda expression. The lambda expression had to go in parentheses just
# for the purposes of grouping all its contents together. Without the extra parentheses around it on line 15,
# the interpreter would group things differently and make a function of x that returns x - 2(6).


def last_char1(s):
    return s[-1]


last_char2 = (lambda s: s[-1])
