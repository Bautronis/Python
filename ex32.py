the_count = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Pears', 'Apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

#same as above
for fruit in fruits:
    print "A fruit of type : %s" % fruit

for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty honey
elements = []

for i in range (0, 6):
    print "adding %d to the list." % i
    #Append is a function that lists Understand
    elements.append(i)

for i in elements:
    print "element was : %d" % i
