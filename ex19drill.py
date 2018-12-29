#A function of my own design and I will try to run in 10 different ways.. atl east
def game_stats (points_ally, points_enemy):
    print "Zalgiris made total points: %d" % points_ally
    print "Grand canaria made total points of: %d" % points_enemy
    if points_ally - points_enemy < 0:
        print "Zalgiris lost a game... Fatality"
    if points_ally - points_enemy >=0 :
        print "Sarunas Jasikevicius won a game"

#Simple arguments
game_stats (80, 70)

#math
game_stats (10+22+33+14, 40+30)

#variables
zalgiris_points = 77
grand_points = 85
game_stats (zalgiris_points, grand_points)

#Variables and a little math
game_stats (zalgiris_points +10, grand_points +8)

#With a variable number of arguments
match_stats = (66, 90)
game_stats(*match_stats)

#Function to functions
def func_to_func():
    value1 = 30
    value2 = 33
    game_stats(value1, value2)
func_to_func()

# a users input
#This should work if I would delete If function
print "How much point Zalgiris made today:"
user_points = raw_input(">>> ")
print "How muhc point Grand Canaria made today?"
user2_points = raw_input(">>>> ")
game_stats (user_points, user2_points)
