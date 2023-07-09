"""
The zip function takes multiple lists and turns them into a list of tuples (actually, an iterator, but they work
like lists for most practical purposes), pairing up all the first items as one tuple, all the second items as a
tuple, and so on. Then we can iterate through those tuples, and perform some operation on all the first items,
all the second items, and so on.
"""
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L4 = list(zip(L1, L2))  # [(3, 1), (4, 2), (5, 3)]
print(L4)

# loop through the tuples:
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = list(zip(L1, L2))
print(L4)  # [(3, 1), (4, 2), (5, 3)]

for (x1, x2) in L4:
    L3.append(x1 + x2)

print(L3)  # [4, 6, 8]

# Or, simplifying and using a list comprehension:
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)  # [4, 6, 8]

print("=====================================\n")
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = list(map(lambda x: x[0] + x[1], zip(L1, L2)))
print(L3)


# HANGMAN GAME
# Consider a function called possible, which determines whether a word is still possible to play in a
# game of hangman, given the guesses that have been made and the current state of the blanked word.

def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True


print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))


# However, we can rewrite that using zip, to be a little more comprehensible:
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True


print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

# Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, L3,
# that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5. This can
# be accomplished in one line of code.
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [value1 + value2 for value1, value2 in zip(L1, L2) if (value1 > 10 and value2 < 5)]
print(L3)
