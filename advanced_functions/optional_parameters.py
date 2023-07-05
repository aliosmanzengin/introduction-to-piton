"""
OPTIONAL PARAMETERS

In the treatment of functions so far, each function definition specifies zero or more formal parameters and each
function invocation provides exactly that many values. Sometimes it is convenient to have optional parameters that
can be specified or omitted. When an optional parameter is omitted from a function invocation, the formal parameter
is bound to a default value. When the optional parameter is included, then the formal parameter is bound to the value
provided. Optional parameters are convenient when a function is almost always used in a simple way, but it’s nice to
allow it to be used in a more complex way, with non-default values specified for the optional parameters.
"""
print(int("100"))
print(int("100", 10))  # same thing, 10 is the default value for the base
print(int("100", 8))  # now the base is 8, so the result is 1*64 = 64

"""When defining a function, you can specify a default value for a parameter. That parameter then becomes an optional 
parameter when the function is called. The way to specify a default value is with an assignment statement inside the 
parameter list. Consider the following code, for example."""

initial = 7

def f(x, y=3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

f(2)
f(2, 5)
f(2, 5, 8)


"""There are two tricky things that can confuse you with default values. The first is that the default value is 
determined at the time that the function is defined, not at the time that it is invoked. So in the example above, 
if we wanted to invoke the function f with a value of 10 for z, we cannot simply set initial = 10 right before 
invoking f. See what happens in the code below, where z still gets the value 7 when f is invoked without specifying a 
value for z."""

initial = 7

def f(x, y=3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

initial = 10
f(2)
f(2, 5)
f(2, 5, 8)


"""The second tricky thing is that if the default value is set to a mutable object, such as a list or a dictionary, 
that object will be shared in all invocations of the function. This can get very confusing, so I suggest that you 
never set a default value that is a mutable object. For example, follow the exceution of this one carefully.
"""

def f(a,L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f(4, ["hello"]))  # ['hello', 4]
print(f(5, ["hello"]))  # ['hello', 5]




