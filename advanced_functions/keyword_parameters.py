# KEYWORD PARAMETERS # https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
"""This is particularly convenient when there are several optional parameters and you want to provide a value for one
of the later parameters while not providing a value for the earlier ones.

In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must match
one of the arguments accepted by the function"""


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

print("\n ======================================================= \n")


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

cheeseshop("AAAAAA")

print("\n ======================================================= \n")

# Keyword Parameters with .format
names_scores = [("Jack", [67, 89, 91]), ("Emily", [72, 95, 42]), ("Taylor", [83, 92, 86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name, s1=scores[0], s2=scores[1], s3=scores[2]))

"""Sometimes, you may want to use the .format method to insert the same value into a string multiple times. You can 
do this by simply passing the same string into the format method, assuming you have included {} s in the string 
everywhere you want to interpolate them. But you can also use positional passing references to do this! The order in 
which you pass arguments into the format method matters: the first one is argument 0, the second is argument 1, 
and so on."""
# this works
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))


