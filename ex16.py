from sys import argv

script, filename = argv

print "we are going to erase %r" % filename
print "if yiu don't want that hit CTRL-C "
print "if you do want that, hit return"


raw_input("?")

print "Opening the file..."
target = open (filename, 'w')
# 'w' is an arguement that puts open() into write mode. It opens by default to
# read mode so to allow write later, we need to set the write flag when we
# actually open the file object. A file object without 'w' can't be written to.
# CAUTION - using 'w' will truncate the file if it already exists!!
print "Truncating the file. Goodbye"

target.truncate()

print "Now I am going to ask you fro three lines"
line1 = raw_input("Line 1 : ")
line2 = raw_input("Line 2 : ")
line3 = raw_input("Line 3 : ")

print "I am going to write these to the file"

# This writes the content of a variable and then a new line over and over
# again in order to format the text in the new file.

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "ANd finally, we close it"
target.close()

# If i put a wrong file name at the begining why it allowed me to run a program.

