#This one is like your scripts with arg
def print_two(*args)
    arg1, arg2 = args
    print "arg1: $r, arg2: %r" % (arg1, arg2)

#that *args is pointless

def print_two_again(arg1, arg2)
    print "arg1: $r, arg2: %r" % (arg1, arg2)

#this just takes one arg
def print_one(arg1)
    print "arg1: %r" % arg1

#this one takes no arg
def print_none()
    print "I got nothing'."

print_two("Zed", "Shaw")
print_two_again ("Zed", "Shaw")
print_one ("First!")
print_none()