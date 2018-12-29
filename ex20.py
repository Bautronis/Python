#functions & files
# Imports the argv function (?) from the sys library
from sys import argv

script, input_file = argv

# Creates a function 'print_all(f)' which reads and prints the input
def print_all(f):
    print f.read()
#read() - return one big string
#readline - return one line at a time
#readlines - returns a list of lines

# Creates a function 'rewind(f)' which sets the input files current position
# to 0 via the 'seek()' function (this is in bytes i.e the start of the file)
def rewind(f):
    f.seek(0)

# Creates a function that accepts an integer (in this case from 'current_line')
# denoting the line to read and then reads that line with the 'readline()'
# function.
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open (input_file)
#open - opens a file

print "First let's print the whole file:\n"

print_all (current_file)

print "Now let's rewind, kind of like a tape."

rewind (current_file)

print "Let's print three lines"

current_line = 1
# Calls function 'print_a_line()' with 'current_line' and 'current_file' as
# parameters.
print_a_line (current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)

#file.seek = seek(...)
    #seek(offset[, whence]) -> None.  Move to new file position.

    #Argument offset is a byte count.  Optional argument whence defaults to
    #0 (offset from start of file, offset should be >= 0); other values are 1
    #(move relative to current position, positive or negative), and 2 (move
    #relative to end of file, usually negative, although many platforms allow
    #seeking beyond the end of a file).  If the file is opened in text mode,
    #only offsets returned by tell() are legal.  Use of other offsets causes
    #undefined behavior.
    #Note that not all file objects are seekable.
