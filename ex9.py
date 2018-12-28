days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nfeb\nMar\nApr\nMay\nJun\nJul\nAug" # \n backflash
# \n won't work with %r, because it's the raw formating for debugging

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want or 5 or 6.
"""