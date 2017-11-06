#!/usr/local/bin/python3
'''
LPTHW exercise 39
A Dictionary Example
'''

# create a mapping of state to abbreviation
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }

# create a basic set of states and some cities in them
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
        }

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State: ", cities['NY'])
print("OR State: ", cities['OR'])

# print out some states
print('-' * 10)
print("Michigan abbreviation: ", states['Michigan'])
print("Florida abbreviation: ", states['Florida'])

# do it via the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has the cities {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by a state that might not be there
state = states.get('Texas')
if not state:
    print("sorry no Texas")

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"the city for the state 'TX' is {city}")
