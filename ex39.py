#create a mapping of state to abbreviation

states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

#create a basic set of states and some cities in them

cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

#add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-'*10)
print("NY State has: ", cities['NY']) # New York
print("OR State has: ", cities['OR']) # Portland

#print some states
print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan']) # MI
print("Florida's abbreviation is: ", states['Florida']) # FL

# do it by using the state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']] ) # Detroit
print("Florida has: ", cities[states['Florida']]) # Jacksonville

# print every state abbreviation
print('-'*10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev)) # Oregon is abbreviated OR etc

#print every city in state
print('-'*10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city)) # CA has the city San Francisco

# now do both at the same time
print('-'*10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))
    # Oregon state is abbreviated OR and has city Portland

print('-'*10)
#safely get abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print("Sorry, no Texas")

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: %s" % city)
# The city for the state TX is : Does not exist
