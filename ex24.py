print "Let's practice everything"
print 'You\'d need to know \'bout escapted with \\ do \n newlines \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovelynor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
"""

print "---------"
print poem
print "---------"

five = 10 - 2 + 3 -  6

print "This should be five : %s" % five

#Function which returns three arguments

def secret_formula (started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

#After that they provides a starting point to a function which is 10k in this case.
start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)

# After this it prints two lines, one of them prints a starting point value
# a second line prints returned value from a function
print "With a starting point of : %d" % start_point
print "We'd have %d beans, %d jars, and %d creates" % (jelly_beans,jars, crates)

#After this they do a little math ^ reduce a starting point value by 10
start_point = start_point / 10


#this time it takes a reduces value of starting point. On top of that
# function is being used at the end of print command .
print "We can also do this way:"
print "we'd have %d beans, %d jars, %d crates" % secret_formula(start_point)
