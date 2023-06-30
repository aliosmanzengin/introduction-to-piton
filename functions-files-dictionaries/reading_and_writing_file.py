"""

open(filename,'r')
    - Open a file called filename and use it for reading. This will return a reference to a file object.
    - Once a file open, it becomes a Python object just like all other data

open(filename,'w')
    - Open a file called filename and use it for writing. This will also return a reference to a file object.
    -if you already have the file u will lose the data.

filevariable.close()
    - File use is complete.

fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for lin in lines:                     # step 3
        #some code that references the variable lin
#some other code not relying on fileref   # step 4

However, this will not be good to use when you are working with large data. Imagine working with a datafile that has
1000 rows of data. It would take a long time to read in all the data and then if you had to iterate over it,
even more time would be necessary. This would be a case where programmers prefer another option for efficiency reasons.


This option involves iterating over the file itself while still iterating over each line in the file:

with open(fname, 'r') as fileref:
 for lin in fileref:
     ## some code that uses line as the current line of the file
     ## some more code

"""

# 1. Open the file using with and open.

# 2. Use .readlines() to get a list of the lines of text in the file.

# 3. Use a for loop to iterate through the strings in the list, each being one line from the file. On each iteration,
# process that line of text

# 4. When you are done extracting data from the file, continue writing your code outside of the indentation. Using
# with will automatically close the file once the program exits the with block.




from faker import Faker

fileref = open("../textFile1.txt", "r")
# contents = fileref.read()  # This will read everything. and not recommended for the sake of saving the memory
# print(len(contents))
# lines = fileref.readlines()  # it returns a list of string one string is for an each line.

for lin in fileref:  # fileref is file object not a list. But we cant take a slice like [:4] it will throw a TypeError
    print(lin.strip())

fileref.close()

fake = Faker(['pl_PL'])
textFile2 = "../textFile2.txt"
file_obj = open(textFile2, "w")

for number in range(13):
    file_obj.write(fake.name())
    file_obj.write('\n')
    print("name written ", number)

file_obj.close()

with open(textFile2, 'r') as md:
    # md.read()
    md.readlines()
    # for lin in md:
    # do something
# "with" is closing the file at the end by itself. No need to add close file
# same thing will work also for writing the files
with open(textFile2, 'w') as md:
    for num in md:
        md.write(str(num) + "\n")
