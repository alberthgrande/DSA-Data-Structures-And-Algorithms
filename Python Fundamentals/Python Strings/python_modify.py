# Python has a set of built-in methods that you can use on strings.

# Upper Case - upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# Lower Case - lower() method returns the string in lower case:
print(a.lower())

# Remove Whitespace - strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String - replace() method replaces a string with another string:
print(a.replace("H", "M").strip())

# Split String 
"""
The split() method returns a list where the text between the specified separator becomes the list items.
The split() method splits the string into substrings if it finds instances of the separator:
"""
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']