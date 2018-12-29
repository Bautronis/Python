# This one is like my scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# OK, that *args is actually pretty pointless, we can just do this
def print_two_again(arg1, arg2):
        print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

#NOTE: args allows you to pass a variable number of arguments to a function
