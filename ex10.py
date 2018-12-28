tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backsflash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list
\t* Cat food
\t* Fishies
\t*Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backsflash_cat
print fat_cat

# \t horizontal TAB
# \' single quote

#Funny code
#while True:
 #   for i in ["/", "-", "|", "\\", "|"]:
  #      print "%s\r" %i

# QUESTION: Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
#A:I would use them because it saves hitting the shift key, which saves some time.

# Study drill code with double/single quotes and %s or %r
print('Didn\'t you see {!r}, that\'s {!r} '.format("Michael\'s tops", "crazy"))
print('Didn\'t you see {!s}, that\'s {!s} '.format("Michael\'s tops", "crazy"))