def double(y):
    y = 2 * y


num = 5
double(num)
print(num)  # 5


def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"


mylst = ['our', 'students', 'are', 'awesome']
changeit(mylst)
print(mylst)  # ['Michigan', 'Wolverines', 'are', 'awesome']

# he state of the list referenced by lst is altered by changeit, and since mylst is an alias for lst,
# mylst is affected by the actions taken by the function.

""" The state of the list referenced by lst is altered by 
changeit, and since mylst is an alias for lst, mylst is affected by the actions taken by the function.

Look closely at this line:
lst[0] = "Michigan" 
    * That statement modifies the state of lst by changing the value in slot 0. Although that line may 
appear to contradict the statement above that “an assignment to a formal parameter inside a function never affects 
the argument in the caller,” note that there is a difference between assigning to a slot of a list, and assigning to 
the list variable itself. To see that difference, try changing that line to the following:

lst = ["Michigan", "Wolverines"] 
    * Then, run again. This time, mylist is not altered. To understand why, use CodeLens 
to step carefully through the code and observe how the assignment to lst causes it to refer to a separate list.

Take a moment to experiment some more with the changeit function. Change the body of the function to the following:
lst.append("Michigan Wolverines")
    * You should see that mylst is affected by this change, 
since the state of the list is altered.

Then, try again with this as the body:
lst = lst + ["Michigan Wolverines"]
    * Here, we create a new list using the concatenation operator, and mylst is not affected by the change.

Understanding the techniques that functions can and cannot use to alter the state of mutable parameters is important. 
"""


def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"
    return lst


mylst = ['106', 'students', 'are', 'awesome']
#newlst = changeit(mylst)
newlst = changeit(list(mylst))  # The built-in list function, which takes a sequence as a parameter and returns a new
                                # list, works to copy an existing list.
                                # For dictionaries, you can similarly call the dict function, passing in a dictionary to get a copy of the dictionary
                                # back as a return value.

print(mylst)  # ['106', 'students', 'are', 'awesome']
print(newlst)  # ['Michigan', 'Wolverines', 'are', 'awesome']


"""
Glossary

argument
A value provided to a function when the function is called. This value is assigned to the corresponding parameter in the function. The argument can be the result of an expression which may involve operators, operands and calls to other fruitful functions.

body
The second part of a compound statement. The body consists of a sequence of statements all indented the same amount from the beginning of the header. The standard amount of indentation used within the Python community is 4 spaces.

calling stack
A sequence (stack) of frames, showing all the function calls that are in process but not yet complete. When one function’s code invokes another function call, there will be more than one frame on the stack.

compound statement
A statement that consists of two parts:

header - which begins with a keyword determining the statement type, and ends with a colon.

body - containing one or more statements indented the same amount from the header.

The syntax of a compound statement looks like this:

keyword expression:
    statement
    statement
    ...
docstring
If the first thing in a function body is a string (or, we’ll see later, in other situations too) that is attached to the function as its __doc__ attribute.

flow of execution
The order in which statements are executed during a program run.

function
A named sequence of statements that performs some useful operation. Functions may or may not take parameters and may or may not produce a result.

function call
A statement that executes a function. It consists of the name of the function followed by a list of arguments enclosed in parentheses.

function composition
Using the output from one function call as the input to another.

function definition
A statement that creates a new function, specifying its name, parameters, and the statements it executes.

fruitful function
A function that returns a value when it is called.

global variable
A variable defined at the top level, not inside any function.

header line
The first part of a compound statement. A header line begins with a keyword and ends with a colon (:)

lifetime
Variables and objects have lifetimes — they are created at some point during program execution, and will be destroyed at some time. In python, objects live as long as there is some variable pointing to it, or it is part of some other compound object, like a list or a dictionary. In python, local variables live only until the function finishes execution.

local variable
A variable defined inside a function. A local variable can only be used inside its function. Parameters of a function are also a special kind of local variable.

method
A special kind of function that is invoked on objects of particular types of objects, using the syntax <expr>.<methodname>(<additional parameter values>)

None
A special Python value. One use in Python is that it is returned by functions that do not execute a return statement with a return argument.

parameter
A name used inside a function to refer to the value which was passed to it as an argument.

return value
The value provided as the result of a function call.

side effect
Some lasting effect of a function call, other than its return value. Side effects include print statements, changes to mutable objects, and changes to the values of global variables.

stack frame
A frame that keeps track of the values of local variables during a function execution, and where to return control when the function execution completes.

type annotation
An optional notation that specifies the type of a function parameter or function result.
"""

