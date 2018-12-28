name = 'Bruno'
age = 24
height = 192
weight = 84
eyes = 'blue'
teeth = 'white'
hair = 'Brown'

#%s paima zodziu reiksme, kai %d skaitine reiksme. %r spausdina ta reiskme "no matter what"

print "let's talk about %r." % name
print "he's %r cm tall." % height
print "he's %r kg heavy" % weight
print "Actually that's not too heavy"
print "he's got %r eyes & %r hair" %(eyes, hair)

print "if I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)

#DRILL 1 . Eliminated my_ in front.


# format characters we can find there:
# https://docs.python.org/3/library/string.html#format-string-syntax

# norint suapvalinti floating number, we need to use function round()