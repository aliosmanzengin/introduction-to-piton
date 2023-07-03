# As a best practice avoid referring to a global variable inside of the function definition

# LOCAL VARIABLE
"""An assignment statement in a function creates a local variable for the variable on the left hand side of the
assignment operator. It is called local because this variable only exists inside the function and you cannot use it
outside.

*  When the execution of the function terminates (returns), the local variables are destroyed.
*  Formal parameters are also local and act like local variables.
"""

# GLOBAL VARIABLE
"""
Variable names that are at the top-level, not inside any function definition, are called global.

It is legal for a function to access a global variable. However, this is considered bad form by nearly all 
programmers and should be avoided."""

"""
def badsquare(x):
    y = x ** power
    return y


power = 2
result = badsquare(10)
print(result)
"""


"""Although the badsquare function works, it is silly and poorly written. We have done it here to illustrate an 
important rule about how variables are looked up in Python. First, Python looks at the variables that are defined as 
local variables in the function. We call this the local scope. If the variable name is not found in the local scope, 
then Python looks at the global variables, or global scope. This is exactly the case illustrated in the code above. 
power is not found locally in badsquare but it does exist globally. The appropriate way to write this function would 
be to pass power as a parameter."""


def powerof(x, p):
    power = p  # Another dumb mistake
    y = x ** power
    return y


power = 3
result = powerof(10, 2)
print(result)


"""The value of power in the local scope was different than the global scope. That is because in this example power 
was used on the left hand side of the assignment statement power = p. When a variable name is used on the left hand 
side of an assignment statement Python creates a local variable. When a local variable has the same name as a global 
variable we say that the local shadows the global. A shadow means that the global variable cannot be accessed by 
Python because the local variable will be found first. This is another good reason not to use global variables. As 
you can see, it makes your code confusing and difficult to understand."""

# If you really want to change the value of a global variable inside a function, you can can do it by explicitly
# declaring the variable to be global, as in the example below. Again, you should not do


def powerof(x,p):
    global power  # a really...
    power = p     # ...bad idea, but valid code
    y = x ** power
    return y


power = 3
result = powerof(10,2)
print(result)  # 100
print(power)  # 2
