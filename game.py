from random import randint

from random import choice

import pprint

from sys import exit

#Setting some core stats
wins = 0
times_trained = 0
gold = randint(1, 3) + 2

# Start Streen
def start_screen():
    print"""
\t\tTHE LEGEND OF DOOBIEUS ARENA

\t\tProgrammed poorly by Ray Weiss
"""
    next()

#Some Quips for the barracks
def gladiator_quips():

    q = []
    q.append('A warrior grunts, "A sword is more versatile than other weapons."')
    q.append('A rogue remarks "Oi I heard that training improves your primary skills."')
    q.append('A wench stats "At least you can fight for your freedom %s."' % character_class)
    q.append('A drunk sings you a song of the legend of Doobieus poorly.')
    q.append('A guard remarks how his polearm gets more lucky hits')
    q.append('A slave mentions that maces pack a heavy punch.')
    q.append('A barkeep laments "I need a vacation."')
    q.append('A one eyed gladiator recalls his youth before slavers killed his family.')
    q.append('A child remarks how training can affect abilities.')
    quips = choice(q)
    print quips


#nice little function that brings up the next page prompt
def next():
    raw_input("Press Enter To Continue...")

# Barracks need to restrict training after training. Also need to
# add training restrictions.
def barracks():
    print  """
Welcome to the barracks %s
                                                    ^^^^ ^^^^^^^^^^^^^^^^
                                                   >----<|arena|training|>
 ~                     MMM    ~                   <|shop<| _   |   __   |>
{ } mmm      ~~~      [~~~]  { } mmm      ~~~     <|    <|{}\  |  /{}\  |>
{ } |||D   _______    [~~~]  { } |||D   _______   <|     -||-  |  -||-  |>
{ } |||   <uuuuuuu>   [~~~]  { } |||   <uuuuuuu>  <|     |||   |   ||   |>
-------------------------------------------------------------------------

There are several other gladiators moving around, you may 'talk' to them.

You can take a look at your 'stats'

You can 'shop' for new weapons.

You may enroll in skill 'training' nearby.

You may face your next opponent in the 'arena'.

You may give up on your quest for freedom & 'quit'

Current HP: %s Gold Pieces: %s
""" % (name, current_hp, gold)

    answer = raw_input(":> ")
    if "talk" in answer:
        gladiator_quips()
        next()
        barracks()
    elif "stats" in answer:
        pp = pprint.PrettyPrinter(indent=30)
        pp.pprint(character_sheet)
        next()
        barracks()
    elif "training" in answer:
        if times_trained == 0:
            train()
        else:
            print "The training center is now closed."
            next()
            barracks()
    elif "arena" in answer:
        combat_engine()

    elif "quit" in answer:
        print "You are now a slave forever. Goodbye %s." % name
        exit(0)
    elif "shop" in answer:
        if wins == 0:
            print "The shop is closed for the day, you must win your first fight"
            next()
            barracks()
        elif wins == 1:
            buy_weapon(level_one_weapons)
        elif wins == 2:
            buy_weapon(level_two_weapons)
        elif wins == 3:
            buy_weapon(level_three_weapons)
        elif wins == 4:
            buy_weapon(level_four_weapons)
        else:
            print "Ray left a bug somewhere. Ballz."
            exit(0)
    else:
        print "I didn't understand %s, please try again." % answer
        next()
        barracks()

#training code
def train_code(stat):
    global gold, times_trained, str, dex, con
    if check != 1:
        gold = gold - 7
        character_sheet.remove(character_sheet[9])
        character_sheet.insert(9, "You have %d gold pieces." % gold)
        if stat == str:
            times_trained = 1
            str = str + 1
            character_sheet.remove(character_sheet[3])
            character_sheet.insert(3, "Strength: %s" % str)
            print "You feel stronger and return to the barracks as training closes."
            next()
            barracks()
        elif stat == dex:
            times_trained = 1
            dex = dex + 1
            character_sheet.remove(character_sheet[4])
            character_sheet.insert(3, "Dexterity: %s" % dex)
            print "You feel dexterous and return to the barracks as training closes."
            next()
            barracks()
        elif stat == con:
            times_trained = 1
            con = con + 1
            character_sheet.remove(character_sheet[5])
            character_sheet.insert(3, "Constiution: %s" % con)
            print "You feel hardier and return to the barracks as training closes."
            next()
            barracks()
        else:
            print "Ray left a stupid bug somewhere"

    else:
        times_trained = 1
        gold = gold - 7
        character_sheet.remove(character_sheet[9])
        character_sheet.insert(9, "You have %s gold pieces." % gold)
        print "You feel like the training was useless. You return to the barracks as training closes."
        next()
        barracks()

# training room
def train():
    global gold, str, dex, con, check
    print  """
Welcome %s to the training center.
You currently have %d gold pieces.

You may enroll in one class before each battle.

Keep in mind, there is a chance you will fail to learn anything.

Training costs 7 gold pieces.

You may train 'str', 'dex', or 'con'

Type 'quit' if you wish to return to the barracks.

Which stat do you wish to train?
    """ % (name, gold)

    answer = raw_input(":> ")
    check = randint(1, 6)
    if 'str' in answer and gold >= 7:
        train_code(str)
    elif 'dex' in answer and gold >= 7:
        train_code(dex)
    elif 'con' in answer and gold >= 7:
        train_code(con)
    elif 'quit' in answer:
        print "You leave the training area."
        next()
        barracks()
    else:
        print """"You either dont have enough gold (%s gp,) or you typed in an error (%s)
""" % (gold, answer)
        next()
        train()

#dice
def d20():
    return randint(1, 20)

def d100():
    return randint(1, 100)

def d6():
    return randint(1, 6)

# Doing Stuff for weapons and the shopkeeper. #################################

def level_zero_price():
    """Generates the price for level one weapons"""
    return randint(1, 3)

def level_one_price():
    """Generates the price for level two weapons"""
    return randint(3, 6)

def level_two_price():
    """Generates the price for level three weapons"""
    return randint(6, 9)

def level_three_price():
    """Generates the price for level four weapons"""
    return randint(9, 12)

def level_four_price():
    "Generates the price for level four weapons"""
    return randint(12, 15)

#weapon inventory code

def weapon_code(weapons):
    global current_weapon
    weapon_choice = raw_input(":> ")
    if weapons[0] in weapon_choice and gold >= sword_price:
        gold_math(sword_price)
        if wins != 0:
            current_weapon = weapons[0]
            inventory(weapons[0])
            character_sheet.remove(character_sheet[10])
            character_sheet.append("Current Weapon: %s" % current_weapon)
            barracks()
        else:
            current_weapon = weapons[0]
            inventory(weapons[0])
            character_sheet.append("Current Weapon: %s" % current_weapon)
            barracks()

    elif weapons[1] in weapon_choice and gold >= blunt_price:
        gold_math(blunt_price)
        if wins != 0:
            current_weapon = weapons[1]
            inventory(weapons[1])
            character_sheet.remove(character_sheet[10])
            character_sheet.append("Current Weapon: %s" % current_weapon)
            barracks()
        else:
            current_weapon = weapons[1]
            inventory(weapons[1])
            character_sheet.append("Current Weapon: %s" % current_weapon)
            barracks()

    elif weapons[2] in weapon_choice and gold >= agile_price:
        gold_math(agile_price)
        if wins != 0:
            current_weapon = weapons[2]
            inventory(weapons[2])
            character_sheet.remove(character_sheet[10])
            character_sheet.append("Current Weapon: %s" % current_weapon)
            barracks()
        else:
            current_weapon = weapons[2]
            inventory(weapons[2])
            character_sheet.append("Current Weapon: %s" % current_weapon)
            barracks()

    elif "quit" in weapon_choice and wins != 0:
            barracks()

    elif "quit" in weapon_choice and wins == 0:
        print "You must buy a weapon first before you can go to the barracks."
        next()
        buy_weapon(level_zero_weapons)

    else:
        print "Either you dont have enough money, or I dont know what %s means" % weapon_choice
        next()
        buy_weapon(weapons)

# price display
def prices(weapons):
    print  """
Please type in the weapon you want to buy.

%s, price: %d gold pieces

%s, price: %d gold pieces

%s, price: %d gold pieces.
""" % (weapons[0], sword_price, weapons[1], blunt_price,weapons[2],
       agile_price)



# gold buying
def gold_math(weapon_price):
    global gold
    character_sheet.remove(character_sheet[9])
    gold = gold - weapon_price
    character_sheet.insert(9, "You have %s gold pieces." % gold)

### Shop / buy weapons room ###############

def buy_weapon(weapons):
    global gold, sword_price, blunt_price, agile_price, current_weapon
    """big bit of code that allows you to buy a weapons from a weapon list.
The function acts a little differently after level zero weapons"""
    global current_weapon
    if weapons == level_zero_weapons:
        sword_price = level_zero_price()
        blunt_price = level_zero_price()
        agile_price = level_zero_price()

        prices(level_zero_weapons)
        weapon_code(level_zero_weapons)
        raw_input("""
Your current weapon is now a %s. Press Enter To Continue
""" % current_weapon)

    elif weapons == level_one_weapons:
        sword_price = level_one_price()
        blunt_price = level_one_price()
        agile_price = level_one_price()

        prices(level_one_weapons)
        weapon_code(level_one_weapons)
        raw_input("""
Your current weapon is now a %s. Press Enter To Continue
""" % current_weapon)

    elif weapons == level_two_weapons:
        sword_price = level_two_price()
        blunt_price = level_two_price()
        agile_price = level_two_price()


        prices(level_two_weapons)
        weapon_code(level_two_weapons)
        raw_input("""
Your current weapon is now a %s. Press Enter To Continue
""" % current_weapon)

    elif weapons == level_three_weapons:
        sword_price = level_three_price()
        blunt_price = level_three_price()
        agile_price = level_three_price()

        prices(level_three_weapons)
        weapon_code(level_three_weapons)
        raw_input("""
Your current weapon is now a %s. Press Enter To Continue
""" % current_weapon)

    elif weapons == level_four_weapons:
        sword_price = level_four_price()
        blunt_price = level_four_price()
        agile_price = level_four_price()

        prices(level_four_weapons)
        weapon_code(level_four_weapons)
        raw_input("""
Your current weapon is now a %s. Press Enter To Continue
""" % current_weapon)

    else:
        print"~~~There is a bug somwhere, forgot to assign (weapons)\n\n\n"

def inventory(current_weapon):
    """Attaches modifiers to secondary stats according to current weapon """
    global mod_dmg, mod_crit

    if current_weapon == level_zero_weapons[0]:
        mod_dmg = dmg
        mod_crit = crit
    elif current_weapon == level_zero_weapons[1]:
        mod_dmg = dmg + 1
        mod_crit = crit
    elif current_weapon == level_zero_weapons[2]:
        mod_dmg = dmg
        mod_crit = crit + 3
    elif current_weapon == level_one_weapons[0]:
        mod_dmg = dmg + 1
        mod_crit = crit + 3
    elif current_weapon == level_one_weapons[1]:
        mod_dmg = dmg + 2
        mod_crit = crit
    elif current_weapon == level_one_weapons[2]:
        mod_dmg = dmg
        mod_crit = crit + 5
    elif current_weapon == level_two_weapons[0]:
        mod_dmg = dmg + 1
        mod_crit = crit + 5
    elif current_weapon == level_two_weapons[1]:
        mod_dmg = dmg + 3
        mod_crit = crit
    elif current_weapon == level_two_weapons[2]:
        mod_dmg = dmg
        mod_dmg = crit + 6
    elif current_weapon == level_three_weapons[0]:
        mod_dmg = dmg + 2
        mod_crit = crit + 5
    elif current_weapon == level_three_weapons[1]:
        mod_dmg = dmg + 4
        mod_crit = crit + 3
    elif current_weapon == level_three_weapons[2]:
        mod_dmg = dmg + 1
        mod_crit = + 8
    elif current_weapon == level_four_weapons[0]:
        mod_dmg = dmg + 3
        mod_crit = crit + 7
    elif current_weapon == level_four_weapons[1]:
        mod_dmg = dmg + 5
        mod_crit = crit + 5
    elif current_weapon == level_four_weapons[2]:
        mod_dmg = dmg + 2
        mod_crit = crit + 10
    else:
        print"There is a bug, ray forgot a weapon or typed shit wrong."
        exit(0)

#End Of Buying / Inventory functions ##########################################

#function for monster damage

def monster_dice(a, b):
    return randint(a, b)

#Function for monster stats
def monster_stats(a, b, c, d):
    global monster_current_hp, monster_crit, monster_dmg, monster_to_hit
    monster_current_hp = a
    monster_crit = b
    monster_dmg = monster_dice(1, c)
    monster_to_hit = d

# Chooses a random monster and sets stats
def choose_monster(monster_list):
    global monster, description
    if monster_list == level_zero_monsters:
        monster = choice(level_zero_monsters)
        if monster == 'wolf':
            monster_stats(4, 5, 6, 12)
            description = "A small and angry dog like creature."
        elif monster == 'goblin':
            monster_stats(5, 7, 5, 10)
            description = "A tiny miserable creature that lives to eat shit."
        elif monster == 'kobold':
            monster_stats(6, 10, 4, 9)
            description = "A small humaniod lizard, very sneaky and annoying"
        else:
            print "Bug in choose monster level 0"
            exit(0)

    elif monster_list == level_one_monsters:
        monster = choice(level_one_monsters)
        if monster == 'orc':
            monster_stats(6, 8, 6, 10)
            description = "A human sized horrid creature, smells awful."
        elif monster == 'gnoll':
            monster_stats(7, 10, 8, 12)
            description = "A large humanoid dog, they can cackle for hours."
        elif monster == 'giant ant':
            monster_stats(8, 7, 7, 11)
            description = "A large and terrifying insect, it makes clicking noises."
        else:
            print "Bug in choose monster level 1"
            exit(0)

    elif monster_list == level_two_monsters:
        monster = choice(level_two_monsters)
        if monster == 'wight':
            monster_stats(9, 10, 10, 12)
            description = "A powerful undead warrior, terrifying in size."
        elif monster == 'komodo dragon':
            monster_stats(7, 12, 8, 10)
            description = "A deadly man sized lizard, very sharp teeth."
        elif monster == 'ogre':
            monster_stats(10, 5, 12, 11)
            description = "A Big and strong stupid ogre."
        else:
            print "Bug in monster level 2"

    elif monster_list == level_three_monsters:
        monster = choice(level_three_monsters)
        if monster == 'troll':
            monster_stats(12, 7, 12, 11)
        elif monster == 'owlbear':
            monster_stats(10, 12, 11, 10)
        elif monster == 'dark priest':
            monster_stats(9, 13, 10, 9)
        else:
            print "Bug in monster level 3"

    elif monster_list == level_four_monsters:
        monster = choice(level_four_monsters)
        if monster == 'dark wizard':
            monster_stats(11, 15, 12, 9)
        elif monster == 'hydra':
            monster_stats(12, 14, 15, 10)
        elif monster == 'stone golem':
            monster_stats(15, 13, 13, 11)
        else:
            print "Problem with monster level 4"
    else:
        print "Ray left diddnt assign a correct choose monster(argv)"
        exit(0)

#Check to hit and applies damage / crit + damage use p for player and m for monster

def hit_check(x):

    global current_hp, monster_current_hp, to_hit, monster_to_hit, crit
    global monster_crit, dmg, monster, monster_dmg

    if x == 'p':
        if d20() >= to_hit and d100() <= crit:
            monster_current_hp = monster_current_hp - dmg * 3
            print "You critically wounded the %s!" % monster
            next()
        elif d20() >= to_hit and d100() > crit:
            monster_current_hp = monster_current_hp - dmg
            print "You wounded the %s!" % monster
            next()
        else:
            print "You missed the %s." % monster
            next()
    elif x == 'm':
        if d20() >= monster_to_hit and d100() <= monster_crit:
            current_hp = current_hp - monster_dmg * 3
            print "The %s critically wounded %s!" % (monster, name)
            next()
        elif d20() >= to_hit and d100() > crit:
            current_hp = current_hp - monster_dmg
            print "The %s wounded %s." % (monster, name)
            next()
        else:
            print "The %s missed %s." % (monster, name)
            next()
    else:
        print "Ray diddnt correctly assign a hit check"
        exit(0)


# Combat engine / prompt

def combat_engine():

    global current_hp, monster_current_hp, wins, gold, hit_points, p, m, wins

    """Will choose a monster, and then allow the player to fight monster"""

    global current_hp, monster_current_hp, prompt

    if wins == 0:
        choose_monster(level_zero_monsters)
    elif wins == 1:
        choose_monster(level_one_monsters)
    elif wins == 2:
        choose_monster(level_two_monsters)
    elif wins == 3:
        choose_monster(level_three_monsters)
    elif wins == 4:
        choose_monster(level_four_monsters)
    else:
        print "bug in choosing monsters over wins"
        exit(0)

    print """
Welcome  %s to the Arena

Today you will be fighting a %s

Description of monster: %s
          """ % (name, monster, description)
    next()

    running = True


    while running:
        if current_hp > 0 and monster_current_hp > 0:
            prompt = raw_input("Type 'a' to attack, 'q' for quit HP: %d :> " % current_hp)
            if prompt == 'a':
                hit_check('p')
                hit_check('m')
        elif current_hp <= 0:
            print "You were killed by the %s, better luck next time." % monster
            exit()
        elif monster_current_hp <= 0:
            print "You defeated the %s! Great Job!" % monster
            next()
            if wins == 0:
                gold_earned = d6() + 2
            elif wins == 1:
                gold_earned = d6() + d6() + 2
            elif wins == 2:
                gold_earned = d6() + d6() + 4
            elif wins == 3:
                gold_earned = d6() + d6() + 5
            elif wins == 4:
                gold_earned = d6() + d6() + 6
            else:
                print "There is a bug you have wins than allowed"
                exit(0)
            if wins != 5:
                gold = gold + gold_earned
                character_sheet.remove(character_sheet[9])
                character_sheet.insert(9, "You have %s gold pieces." % gold)
                print "You win %d gold, you have %d gold total." % (gold_earned,
                                                                gold)
                times_trained = 0
                wins = wins + 1
                hit_points = hit_points + d6()
                current_hp = hit_points
                character_sheet.remove(character_sheet[8])
                character_sheet.insert(8, "Hit Points: %d/%d" % (hit_points, current_hp))
                print "You feel hardier. You make your way back to the barracks."
                next()
                barracks()
            else:
                you_win()

        else:
            print "Bug in combat engine"
            exit(0)

def you_win():
 print  """
 YOU WIN!

 CONGRATULATIONS!

 THANKS FOR PLAYING!
 """


# Monster List
level_zero_monsters = ['wolf', 'goblin', 'kobold']
level_one_monsters = ['orc', 'gnoll', 'giant ant',]
level_two_monsters = ['wight', 'komodo dragon', 'ogre']
level_three_monsters = ['troll', 'owlbear', 'dark priest']
level_four_monsters = ['dark wizard', 'hydra', 'stone golem']

# Weapon lists
level_zero_weapons = ['short sword', 'club', 'dagger']
level_one_weapons = ['sword', 'mace', 'rapier']
level_two_weapons = ['long sword', 'morningstar', 'trident']
level_three_weapons = ['claymore', 'flail', 'sycthe']
level_four_weapons = ['bastard sword', 'dragon bone', 'crystal halbred']

def roll_3d6():
    """This rolls 3D6, and returns the sum."""
    return randint(1, 6) + randint(1, 6) + randint(1, 6)

def character_gen():
    """Creates A character and also can call character sheet"""
    global name, str, dex, con, hit_points, dmg, crit, character_class
    global gender, damage_print, current_hp, character_sheet, to_hit

    character_sheet = []
    name = raw_input("Please tell me your name brave soul. :> ")

    print "\n\t\tLets now randomly generate brave gladiator %s." % name

    str = roll_3d6()
    if str > 12:
        dmg = randint(1, 6) + 1
        damage_print = "1D6 + 1"
    else:
        dmg = randint(1, 6)
        damage_print = "1D6"

    dex = roll_3d6()
    if dex >= 13:
        crit = 15
        to_hit = 9
    elif dex >= 9 and dex <=12:
        crit = 10
        to_hit = 10
    else:
        crit = 10
        to_hit = 11

    con = roll_3d6()
    if con > 14:
        hit_points = 8
        current_hp = hit_points
    else:
        hit_points =  6
        current_hp = hit_points

    if str >= dex:
        character_class = "Warrior"
    else:
        character_class = "Rogue"

    random_gender = randint(1, 2)
    if random_gender == 1:
        gender = "Male"
    else:
        gender = "Female"

    character_sheet.append("Name: %s:" % name)
    character_sheet.append("Gender: %s" % gender)
    character_sheet.append("Character Class: %s" % character_class)
    character_sheet.append("Strength: %s" % str)
    character_sheet.append("Dexterity: %s" % dex)
    character_sheet.append("Constitution: %s" % con)
    character_sheet.append("Damage %s" % damage_print)
    character_sheet.append("Crit Chance {}%".format(crit))
    character_sheet.append("Hit Points: %s/%s" % (hit_points, current_hp))
    character_sheet.append("You have %s gold pieces." % gold)

    pp = pprint.PrettyPrinter(indent=30)
    pp.pprint(character_sheet)
    raw_input("Please Press Enter To Buy A Weapon")
    buy_weapon(level_zero_weapons)

#main
start_screen()
character_gen()
