#create a mapping of state to abbreviation州字典
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michegen' : 'MI'
}

#Create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

#add some more cities给城市字典添加映射
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-'*10)
print("NY State has: ",cities['NY'])
print("OR State has: ",cities['OR'])

#print some states
print('-'*10)
print("Michegen's abbreviation is: ",states['Michegen'])
print("Florida's abbreviation is: ",states['Florida'])

#do it by using the state then cities dict
print('-' * 10)
print("Michegen has: ",cities[states['Michegen']])
print("Florida has is: ",cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has city {city}")

#now do both at the same time
print('-' * 10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev} ")
    print(f" and has city {cities[abbrev]}")

print('-' * 10)
#safely get a abbreviation by state that might not be here
state = states.get('Texas')

if not state:
    print("Sorry,no Texas.")

#Get a city with a default value
city = cities.get('TX','Does not Exist')
print(f"The city for the state 'TX' is: {city}" )