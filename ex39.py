#Creates a mapping of states

states = {
    'Oregon'     : 'OR',
    'Ohio'       : 'OH',
    'California' : 'CA',
    'New York'   : 'NY',
    'Michigan'   : 'MI'
}

# Creates a list of cities which are linked to a state

cities = {
    'CA': 'San Francisco',
    'OH': 'Cleveland',
    'FL': 'FT. Meyers',
    'MI': 'Ann Arbor'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print "-" * 20
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print "-" * 20
print "Ohio's abbr is: ", states['Ohio']
print "Michigan's abbr is: ", states['Michigan']

print "-" * 20
for state, abbr in states.items():
    print "%s is abbr'd %s." % (state, abbr)

print "-" * 20
for abbr, city in cities.items():
    print "%s has the city %s" % (abbr, city)

print "-" * 20
for state, abbr in states.items():
    print "%s is abbr'd %s and has the city %s." % (state, abbr, cities[abbr])

print "-" * 20
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

cities = cities.get('TX', 'Does Not Exist')
print "The city for 'TX' is: %s" % city

#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and values
#get()	Returns the value of the specified key
#items()	Returns a list containing the a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary