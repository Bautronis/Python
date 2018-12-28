from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, Im the %s script" % (user_name, script)
print "Id like to ask you a few Q"
print "do you like me %s" % user_name
likes = raw_input(prompt)

print "where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
So you said %r about liking me.
\nYou live in %r. 
\nYou have a %r car. P
""" % (likes, lives, computer)