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