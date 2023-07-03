# The syntax for creating a named function, a function definition, is:

def hello():
    """This function says hello and greets you"""  # docstring
    print("Hello")  # statement
    print("Glad to meet you")  # statement


"""Another way to retrieve this information is to use the interactive interpreter, and enter the expression 
<function_name>.__doc__, which will retrieve the docstring for the function. So the string you write as documentation 
at the start of a function is retrievable by python tools at runtime. This is different from comments in your code, 
which are completely eliminated when the program is parsed.

By convention, Python programmers use docstrings for the key documentation of their functions."""

# Defining a new function does not make the function run.
# To execute the function, we need a function call. This is also known as a function invocation.

hello()
print(type(hello))  # <class 'function'>


# A function needs certain information to do its work. These values, often called arguments or actual parameters or
# parameter values, are passed to the function by the user.

# In the definition, the parameter list is sometimes referred to as the formal parameters or parameter names.
# These names can be any valid variable name. If there is more than one, they are separated by commas.

def hello2(s):
    print("Hello " + s)
    print("Glad to meet you")


hello2("Iman" + " and Jackie")
hello2("Class " * 3)

"""Functions that return values are sometimes called fruitful functions. In many other languages, a function that 
doesn’t return a value is called a procedure, but we will stick here with the Python way of also calling it a 
function, or if we want to stress it, a non-fruitful function."""


def square(x):
    y = x * x
    return y


toSquare = 10
result = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, result))


# Type Annotations Python allows you to indicate the intended type of the function parameters and the type of the
# function return value in a function definition using a special notation demonstrated in this example:

def duplicate(msg: str) -> str:
    """Returns a string containing two copies of `msg`"""

    return msg + msg


result = duplicate('Hello')
print(result)


def add(x: int, y: int) -> int:
    """Returns the sum of `x` and `y`"""

    return x + y


def get_number(msg: str) -> float:
    """Prompts with `msg` for input; returns numeric response."""

    return float(input(msg))


def display_msg(msg: str):
    """Displays `msg` with dashed line underneath"""

    print(msg)
    print('-------------------------------------')


"""It’s important to understand that adding type annotations to a function definition does not cause the Python 
interpreter to check that the values passed to a function are the expected types, or cause the returned value to be 
converted to the expected type."""






