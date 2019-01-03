
from random import randint

from random import choice

import pprint
import random

from sys import exit

energy = randint(1, 10) + 5
water = randint(0, 1)

def start():
    global energy
    print "You are in the the middle of nowhere. You don't remember anything"
    print "You have %r energy left. Keep in mind before doing smth" % energy
    print "You can take go to the 'right' or to the 'left'"
    print "There are several ghost moving around, you may 'talk' to them. "
    print "You may give up on your journey & 'quit'"


    choice = raw_input("> ")

    if choice == "talk":
        energy = energy - 1
        people_quips()
        next()
        start()

    if choice == "quit":
        dead()

    if choice == "left":
        energy = energy - 4
        left_road()

    elif choice == "right":
        energy = energy - 10
        right_road()
    else:
        print "You are doomed forever."

def next():
    raw_input("Press Enter To Continue...")

def stats():
    global energy
    print " &r Energy remaining" % energy

def dead():
    print "You are dead."

def right_road():
    if energy <= 0:
        print "After a long jorney you run of food & water and you collapsed."

def people_quips():

    q = []
    q.append('A which says, "Heres looking at you, kid"')
    q.append('A rabit remarks "Go ahead, make my day."')
    q.append('A taxi driver shouts "You talking to me?"')
    q.append('A drunk sings you a song of the legend of Doobieus poorly.')
    q.append('A guard remarks how his polearm gets more lucky hits')
    q.append('A slave mentions that maces pack a heavy punch.')
    q.append('Yankee says "Today, I consider myself the luckiest man on the face of the earth."')
    q.append('Animal "One morning I shot an elephant in my pajamas. How he got in my pajamas, I dont know"')
    q.append('A soldier remarks Gentlemen that I cant fight in here! This is the War Room')
    quips = choice(q)
    print quips

def left_road():
    global energy
    print "After a long journey you reached ruins."
    print "There are several ghost moving around, you may 'talk' to them. "
    print "You can go to 'catacombs' or 'church' "
    print "You can check your energy by checking your'stats'"

    choice_left = raw_input(" > ")

    if choice_left == "talk":
        energy = energy - 1
        people_quips()
        next()
        left_road()

    elif choice_left == "stats":
        print "You have %d energy left" % energy
        next()
        left_road()

    elif choice_left == "church":
        church()

    elif choice_left == "catacombs":
        catacombs()

    elif energy <= 0:
        dead()

    else:
        print "You can do that. You don't have a time"
        next()
        left_road()

def church():
    global energy
    energy = energy - 2
    print "You lost 2 energy, because there is obstacles in the way"
    print "In the church there is a bottle of water."
    print "Are you going to drink this? This is a good opportunity to restore energy"
    print "Anytime you can go 'back'"

    choice_water = raw_input()
    global water

    if choice_water == "yes" and water == 1:
        print "You restored 15 energy. Currently you have %d" % energy
        next()
        church()

    elif choice_water == "yes" and water == 0:
        print "Water was poisoned. You lost 5 energy. Currently you have %d " % energy
        next()
        church()
    elif choice_water == "back":
        energy = energy - 2
        next()
        left_road()
    else:
        print "Wrong answer."
        next()
        left_road()

    if energy <= 0:
        dead()

def catacombs():
    global energy
    energy = -2
    print "You lost 2 energy, it was a long road."
    print "You see a door in fron of you"
    print "There is a dice next to these doors"
    print "There is a legend that in order for these doors to be opened you need to roll out 5"
    print "If you won't roll out 10 in 3 times you will be cursed"
    print "You can 'try' to roll the dice or go 'back'. Anytime you can check the 'stats'."

    catacombs_choice = raw_input( " > ")

    if catacombs_choice == "talk":
        energy = energy - 1
        people_quips()
        next()
        catacombs()

    elif catacombs_choice == 'back':
        energy= energy - 2
        left_road()

    elif catacombs_choice == "try":
        i = 0
        roll_again = "yes"

        while roll_again == "yes" or roll_again == "y" and i < 10:
            i= i + 1
            random = randint (1, 6)
            print "Rolling the dices %d time..." % i
            print "The values are...."
            print random

            if random == 5:
                print "you won the game"
                exit()

            else:

                roll_again = raw_input("Roll the dices again?")


        else:
            print "Ancient curse was casted on you"
            dead()

    elif catacombs_choice == "stats":
        print "You have %d energy left" % energy
        next()
        catacombs()

    if energy <= 0:
        dead()



start()
