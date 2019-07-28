# F strings
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


#start from Avoiding Index Errors in ch3