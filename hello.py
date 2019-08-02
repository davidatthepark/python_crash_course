# Ch 1 - 3
print('\n------ Ch 1 - 3 -------\n')

# F strings. Basically string interpolation.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {full_name.title()}!"
print(message)
print("{} {}".format(first_name, last_name).title())

# Whitespace, tabs, newlines
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
favorite_language = 'python'
print(favorite_language.rstrip())
print(favorite_language.strip())
print(favorite_language.lstrip())

# Ch 3 Lists
bicycles = ['trek', 'cannondale', 'redline']
print(bicycles[-2]) # returns second to last element
print(f'my first bicycle was a {bicycles[-1]}')
bicycles.append('schwinn') # adds an entry
del bicycles[1] # removes cannondale
# pop can also delete at any index. Use it when you 
# want to return the popped value.
bicycles.remove('trek') # removes trek
print(bicycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) # mutates original array
print(cars)
print(sorted(cars)) # does not mutate original array
print(cars) # does not mutate original array
print(len(cars))

# Ch 4: Working With Lists
print('\n------ Ch 4 -------\n')

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')

for number in range(1, 21):
    print(number)

million_numbers = range(1, 1_000_001)
#for number in million_numbers:
#    print(number)

print(sum(million_numbers))

odd_numbers = range(1, 21, 2)
for number in odd_numbers:
    print(number)

for number in range(1, 11):
    print(number**3)

print([value**3 for value in range(1, 11)])

# Working with part of a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Same as JS slice. Can omit the first and/or last index.
print(players[0:3]) 
print(players[-2:])
print('\n')
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

# Tuples - Immutable list
print('\nTuples')
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print('\n')
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f'Requested {topping}')
else:
    print("Are you sure you want no toppings?")

# Dictionaries - Basically JS objects
print('\n')
alien_0 = {'color': 'green', 'job': 'alien', 'weapon': 'banana'}
print(alien_0['color'])
# Use get when the key might not exist
print(alien_0.get('height', 'no such value')) 

for k, v in alien_0.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")

# Can wrap these dictionaries in methods like sorted or set.
for key in alien_0.keys():
    print(f'{key}')

# 8-7
def make_album(artist_name, album_title):
    return {
        
    }