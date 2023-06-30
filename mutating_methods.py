"""unlike strings, lists are mutable. This means we can change an item  in a list by accessing it directly as part of
the assignment statement.

"""

fruit = ["banana", "apple", "cherry"]
print(fruit)
fr = fruit  # fr and fruit have same reference
print(fr)
fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)
print(fr)

a = "aaa"

print(a[0].upper())
print(". ".join(fruit))
print(fruit)
