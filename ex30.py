people = 30
cars = 40
buses = 15

if cars > people:
    print "we should take the cars"
elif cars < people:
    print "we should not take the cars"
else:
    print "we can't decide"

if buses > cars:
    print "THat's too many buses"
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide"

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then"

#The else statement is an optional statement and there could be at most
#only one else statement following if.

#The elif statement allows you to check multiple expressions for TRUE and
#execute a block of code as soon as one of the conditions evaluates to TRUE.

#Similar to the else, the elif statement is optional. However, unlike else,
#for which there can be at most one statement, there can be an arbitrary number
#of elif statements following an if.

#example:
var = 100
if var == 200:
   print "1 - Got a true expression value"
   print var
elif var == 150:
   print "2 - Got a true expression value"
   print var
elif var == 100:
   print "3 - Got a true expression value"
   print var
else:
   print "4 - Got a false expression value"
   print var

print "Good bye!"

#note: if multiple elif are true, it rwill run only the first one
