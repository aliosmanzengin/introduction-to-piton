# WHILE LOOP
"""The for statement will always iterate through a sequence of values like the list of names for the party or the
list of numbers created by range. Since we know that it will iterate once for each value in the collection,
it is often said that a for loop creates a definite iteration because we definitely know how many times we are going
to iterate. On the other hand, the while statement is dependent on a condition that needs to evaluate to False in
order for the loop to terminate. Since we do not necessarily know when this will happen, it creates what we call
indefinite iteration. Indefinite iteration simply means that we don’t know how many times we will repeat but
eventually the condition controlling the iteration will fail and the iteration will stop. (Unless we have an infinite
loop which is of course a problem)"""


import random


def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """

    theSum = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum


print(sumTo(10))
print(sumTo(100))
print(sumTo(1000))
print(sumTo(10000))


def stop_at_four(li1):
    """HALT!"""
    li2 = []
    i = 0
    while li1[i] != 4:
        li2.append(li1[i])
        i += 1
    return li2


print(stop_at_four([1, 2, 3, 4]))

# The Listener Loop
# Inside the while loop there is a function call to get user input. The loop repeats indefinitely,
# until a particular input is received.Inside the while loop there is a function call to get user input. The loop
# repeats indefinitely, until a particular input is received.
theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum = theSum + x

print(theSum)


# Sentinel Values
# * total - this will start at zero
# * count - the number of items, which also starts at zero
# * moreItems - a boolean that tells us whether more items are waiting; this starts as True
# In this program, zero is a sentinel value, a value used to signal the end of the loop. Here’s the code:
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        elif price == 0 and total == 0:
            print("cancelled")
            print('Total items:', count)
            print('Total $', total)
            return
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)


checkout()


# Validating Input
# You can also use a while loop when you want to validate input; when you want to make sure the user
# has entered valid input for a prompt. Let’s say you want a function that asks a yes-or-no question. In this case,
# you want to make sure that the person using your program enters either a Y for yes or N for no (in either upper or
# lower case). Here is a program that uses a while loop to keep asking until it receives a valid answer. As a preview
# of coming attractions, it uses the upper() method which is described in String Methods to convert a string to upper
# case. When you run the following code, try typing something other than Y or N to see how the code reacts:
def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()  # convert to upper case
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer


response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')
if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')

