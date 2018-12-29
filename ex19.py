#creates a function with two arugments
def cheese_and_crackers (cheese_count, boxes_of_crackers):
    #prints the value of "cheese_count" in a string using digit formatter
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    #prints a string
    print "Man that's enough for a party"
    print "Get a blanket.\n"

print "we can just give the functions numbers directly:"
# calls the function "cheese_and_crackers" with argument value of 20 and 30
cheese_and_crackers(20, 30)

print "Or we can use variables from our scripts"
amount_of_cheese = 10
amount_of_crackers = 50
# call the function "cheese_and_crackers" with arguments set to the variables
# "amount_of_cheese" and "amount_of_crackers", whose values respectively are
# set to "10" and "50".
cheese_and_crackers (amount_of_cheese, amount_of_crackers )

print "We can even do math inside too"
# calls the function "cheese_and_crackers" with the arguments "10+20" and "5+6"
# which proves it's possible to do math on the arguments/values passed to the
# function
cheese_and_crackers (10+20, 5+6)

print "We can combine the two, variables and math"
# calls the function "cheese_and_crackers" with the arguments
# "amount_of_cheeses+100" and "amount_of_crackers +1000" which proves it's
# possible to do math on the variables passed to the function
cheese_and_crackers (amount_of_cheese + 100, amount_of_crackers + 1000)
