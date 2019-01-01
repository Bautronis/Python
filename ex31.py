print "You enter a dark room with two doors. Do you go through door #1 or door #2?"
door = raw_input (" > ")
if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake"
    print "2. Scream at the bear."

    bear = raw_input(" > ")

    if bear == "1":
        print "The bear eats your face off. "
        print "GAME OVER"
    elif bear == "2":
        print "The bear eats your legs off. You are still alive.."
        print "You see next to you is backpack, there you can find a cellphone and badages."
        print "In order to get there you need to ger rid of bear, what you are going to do about this?"
        print "1. Don't move. The bear will go away"
        print "2. Scream for a help"
        print "3. Throw a honey as a bait"

        choice = raw_input (" > ")

        if choice == "1":
            print "You made a right desicion. Bear went away. You have time to badgage yourself"
        else:
            print "GAME OVER."
    else:
        print "well, doing %s is probably better. Bears runs away" % bear

elif door == "2":
    print "You have stare into the endless abyss at the Cthulhu's retina"
    print "1. Blueberries"
    print "2. Yellow jacker clothespins"
    print "3. Understanding revolvers yelling melodies"

    insanity = raw_input(" > ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello."
    else:
        print "The insanity rots your eyes into a pool of muclk"

else:
    print "You stumble around and fall on a kinfie and die."
