ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that"

stuff = ten_things.split (' ')
more_stuff = [ "day", "night", "song", "Frisbee", "Corn", "Banana", "girl", "boy"]

while len(stuff) != 10 :
    next_one = more_stuff.pop() #.pop() removes the last item in the list & brings it back
    print "Adding : ", next_one
    stuff.append(next_one) # append function; Add an item to the end of the list
    print "There is %d items now" %len(stuff)

print "There we go:", stuff

print "Lets do some thing with stuff"
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

