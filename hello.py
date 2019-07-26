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

# continue on the zen of python