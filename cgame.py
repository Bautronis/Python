

from sys import exit
from random import randint
import random


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

#Pacios programos pagrindine dalis, kurioje aprasoma scenos ir kas o kurios turi eitiself.
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

#Pabaigos scena, kurioje ismeta viena is pasirinktu eiluciu
class Death(Scene):

    quips = [
        "You are out of money. Your wife is going to kill you...",
         "Never thought you are so good at loosing.. ",
         "Such wow",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

#Pagridine zaidimo dalis, kurioje yra galimybe islosti pinigu suma
#Zaidimas pasibaigs arba kai pralosi visus pinigus arba kai turesi daugiau nei 100$

#!!!!! Dabartine dilema kaip grazinti i pagrindini koridoriu bei tuo paciu metu grazinti skaitine verte
class CentralCorridor(Scene):

    def enter(self):
        wallet = 50
        print "Currently you have : %d " %wallet
        print "Are you going to play?"
        answer = raw_input (" ---->")

        if wallet > 100:
            return 'finished'

        else answer == 'Yes':
            print "How much money do you want to bet? A win rate 3x. "
            bet = int(raw_input("Enter a number: "))
            deck = Deck()
            hand = deck.deal(3)
            print(" - ".join(map(str, hand)))
            if min(hand[0], hand[1]) < hand[2] < max(hand[0], hand[1]):
                print "You won a bet! "
                #prize = bet * 3
                print "You betted %d & won %d", (bet, prize)
                return 'central_corridor',
            else:
                print "You lost a bet"
                #lost = bet
                return 'central_corridor'

        elif:
            return 'death'



class Finished(Scene):

    def enter(self):
        print "Croupier is out of money... He left a game. You wifi is proud!"
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Card(object):

    FACES = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        value = self.FACES.get(self.rank, self.rank)
        return "{0} of {1}".format(value, self.suit)

    def __lt__(self, other):
        return self.rank < other.rank


class Deck(object):

    def __init__(self, ranks=None, suits=None):
        if ranks is None:
            ranks = range(2, 15)
        if suits is None:
            suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
##        self.deck = [Card(r, s) for r, s in product(ranks, suits)]
        self.deck = []
        for r in ranks:
            for s in suits:
                self.deck.append(Card(r, s))

    def deal(self, n):
        return random.sample(self.deck, n)

#Uzkraunam zaidima
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
