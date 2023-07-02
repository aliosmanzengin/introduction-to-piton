"""
 Note that the trick of splitting the text for each row based on the presence of commas only works because commas are
  not used in any of the field values. Suppose that some of our events were more specific, and used commas. For example,
  “Swimming, 100M Freestyle”. How will a program processing a .csv file know when a comma is separating columns,
  and when it is just part of the text string giving a value within a column?

The CSV format is actually a little more general than we have described and has a couple of solutions for that problem.
 One alternative format uses a different column separator, such as | or a tab (t). Sometimes, when a tab is used,
 the format is called tsv, for tab-separated values). If you get a file using a different separator,
 you can just call the .split('|') or .split('\\t').

The other advanced CSV format uses commas to separate but encloses all values in double quotes.

For example, the data file might look like:

"Name","Sex","Age","Team","Event","Medal" "A Dijiang","M","24","China","Basketball","NA" "Edgar Lindenau Aabye","M",
"34","Denmark/Sweden","Tug-Of-War","Gold" "Christine Jacoba Aaftink","F","21","Netherlands","Speed Skating, 1500M",
"NA" If you are reading a .csv file that has enclosed all values in double quotes, it’s actually a pretty tricky
programming problem to split the text for one row into a list of values. You won’t want to try to do it directly.
Instead, you should use python’s built-in csv module.

 """

fileconnection = open("../data_sources/olympics.txt", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}: {}; {}".format(
                vals[0],
                vals[4],
                vals[5]))

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("../data_sources/reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
#    row_string = ','.join([olympian[0], str(olympian[1]), olympian[2]])   #  2nd option
#    row_string = ','.join(olympian) ----> this will work if all elements in the list are string
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()


# for data contains comma and quotes marks
olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
