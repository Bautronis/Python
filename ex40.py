class Song(object):
    # _init_ funct is used to initialize (e.g., specify) an object’s initial attributes by giving them their default value (or state)
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        """Sings a song's lyrics"""
        for line in self.lyrics:
            print line

happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"
])

bulls_on_parade = Song([
    "They rally around the family",
    "With pockets full of shells"
])

happy_bday.sing_me_a_song()

print "-" * 40

bulls_on_parade.sing_me_a_song()

