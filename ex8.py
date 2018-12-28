formatter = "%r %r %r %r"

print formatter % (1, 2, 3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "Ho ho ho",
    "Kaledu senelis stai cia.",
    "Kas noretu dovanu?",
    "Jei norit dovanu, turit pasakyti eilarastuka"
)
