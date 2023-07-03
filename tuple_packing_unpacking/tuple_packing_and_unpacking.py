# Wherever python expects a single value, if multiple expressions are provided, separated by commas,
# they are automatically packed into a tuple. For example, we can omit the parentheses when assigning a tuple of
# values to a single variable.

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# or equivalently
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"

print(julia[4])

"""Functions can return tuples as return values. This is very useful — we often want to know some batsman’s highest 
and lowest score, or we want to find the mean and the standard deviation, or we want to know the year, the month, 
and the day, or if we’re doing some ecological modeling we may want to know the number of rabbits and the number of 
wolves on an island at a given time. In each case, a function (which can only return a single value), can create a 
single tuple holding multiple elements."""


def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a


print(circleInfo(10))


def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a


print(circleInfo(10))

circumference, area = circleInfo(10)
print(circumference)
print(area)

circumference_two, area_two = circleInfo(45)
print(circumference_two)
print(area_two)

# Python has a very powerful tuple assignment feature that allows a tuple of variable names on the left of an
# assignment statement to be assigned values from a tuple on the right of the assignment. Another way to think of
# this is that the tuple of values is unpacked into the variable names.
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"

name, surname, birth_year, movie, movie_year, profession, birth_place = julia
# This does the equivalent of seven assignment statements, all on one easy line.

# (a, b, c, d) = (1, 2, 3) # ValueError: need more than 3 values to unpack

# NOTE
# Unpacking into multiple variable names also works with lists, or any other sequence type, as long as there is
# exactly one value for each variable.
# For example, you can write x, y = [3, 4].

# This feature is used to enable swapping the values of two variables. With conventional assignment statements,
# we have to use a temporary variable. For example, to swap a and b:
a = 1
b = 2
temp = a
a = b
b = temp
print(a, b, temp)

# Tuple assignment solves this problem neatly:
a = 1
b = 2
(a, b) = (b, a)
print(a, b)
# The left side is a tuple of variables; the right side is a tuple of values. Each value is assigned to its
# respective variable. All the expressions on the right side are evaluated before any of the assignments. This
# feature makes tuple assignment quite versatile.


authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)

# Python provides a built-in function enumerate. It takes a sequence as input and returns a sequence of tuples. In
# each tuple, the first element is an integer and the second is an item from the original sequence. (It actually
# produces an “iterable” rather than a list, but we can use it in a for loop as the sequence to iterate over.)
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for item in enumerate(fruits):
    print(item[0], item[1])

print(enumerate(fruits))
print(type(enumerate(fruits)))

track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3,
                      'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0,
                      '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}

track_events = []

for k, v in track_medal_counts.items():
    track_events.append(k)

print(track_events)


def add(x, y):
    return x + y


print(add(3, 4))
z = (5, 4)
# print(add(z)) # this line causes an error
print(add(*z))  # UNPACKING

lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'),
            ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'),
            ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'),
            ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]

t_check = [tup[2] for tup in lst_tups if len(tup) >= 3]

print(t_check)
