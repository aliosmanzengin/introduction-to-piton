# If we want to find out how often the letter ‘t’ occurs, we can accumulate the result in a count variable.

f = open('../data_sources/scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0  # initialize the accumulator variable
for c in txt:
    if c == 't':
        t_count = t_count + 1  # increment the counter
print("t: " + str(t_count) + " occurrences")

f.close()
print("\n*********************************************\n")

# We can accumulate counts for more than one character as we traverse the text. Suppose, for example, we wanted to
# compare the counts of ‘t’ and ‘s’ in the text.
f = open('../data_sources/scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0  # initialize the accumulator variable
s_count = 0  # initialize the s counter accumulator as well
for c in txt:
    if c == 't':
        t_count = t_count + 1  # increment the t counter
    elif c == 's':
        s_count = s_count + 1
print("t: " + str(t_count) + " occurrences")
print("s: " + str(s_count) + " occurrences")
f.close()
print("\n*********************************************\n")

# Rather than pre-specifying which letters to keep accumulator counts for, we can start with an empty dictionary and
# add a counter to the dictionary each time we encounter a new thing that we want to start keeping count of.

f = open('../data_sources/scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {}  # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    # whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

print("t: " + str(letter_counts['t']) + " occurrences")
print("s: " + str(letter_counts['s']) + " occurrences")
print(letter_counts)

f.close()
print("\n*********************************************\n")

# Notice that in the for loop, we no longer need to explicitly ask whether the current letter is an ‘s’ or ‘t’. The
# increment step on line 11 works for the counter associated with whatever the current character is. Our code is now
# accumulating counts for all letters, not just ‘s’ and ‘t’.

# As a final refinement
f = open('../data_sources/scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {}  # start with an empty dictionary
for c in txt:
    letter_counts[c] = letter_counts.get(c, 0) + 1

print("t: " + str(letter_counts['t']) + " occurrences")
print("s: " + str(letter_counts['s']) + " occurrences")
print(letter_counts)
f.close()
print("\n*********************************************\n")

f = open('../data_sources/scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0

    letter_counts[c] = letter_counts[c] + 1

# Write a loop that prints the letters and their counts
for char in letter_counts:
    print(char, ":", letter_counts[char])

f.close()
print("\n*********************************************\n")

# In the solution to the problem above, note that only those letters that actually occur in the text are shown. Some
# punctuation marks that are possible in English, but were never used in the text, are omitted completely. The blank
# line partway through the output may surprise you. That’s actually saying that the newline character, \n,
# appears 5155 times in the text. In other words, there are 5155 lines of text in the file. Let’s test that
# hypothesis. Run the following example and check its output:
f = open('../data_sources/scarlet.txt', 'r')
txt_lines = f.readlines()
# now txt_lines is a list, where each item is one
# line of text from the story
print(len(txt_lines))

f.close()
print("\n*********************************************\n")

# Split the string sentence into a list of words, then create a dictionary named word_counts that contains each word
# and the number of times it occurs.
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

word_counts = {}
for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print("\n*********************************************\n")

# Write a program that finds the key in a dictionary that has the maximum value. If two keys have the same maximum
# value, it’s OK to print out either one. Fill in the skeleton code
d = {'a': 194, 'b': 54, 'c': 34, 'd': 44, 'e': 312, 'full': 31}

ks = d.keys()
best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
for k in ks:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

print("\n*********************************************\n")
# Create a dictionary called d that keeps track of all the characters in the string placement and notes how many
# times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to
# min_value.

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit " \
            "Mackinaw later since the island is a cool place to explore."
"""
d = {}
for i in placement:
    d[i] = d.get(i, 0) + 1

min_value = list(d.keys())[0]
for i in d:
    if d[min_value] < d[i]:
        min_value = d[i]
        print(min_value)
        """

