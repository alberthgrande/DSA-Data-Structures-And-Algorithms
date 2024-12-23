# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(a)
# print("\n")

# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
# print(a)
# print("\n")

# Strings are Arrays
a = "Hello, World!"
# print(a[1])
# print("\n")

"""
Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.
"""

# for x in "banana":
#   print(x)
# print("\n")
  
"""
String Length
To get the length of a string, use the len() function.
"""
a = "Hello, World!"
# print(len(a))

"""
Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.
"""
txt = "The best things in life are free!"
# print("free" in txt)

# Use it in an if statement:
txt = "The best things in life are free!"
# if "the" in txt:
#   print("Yes, 'free' is present.")
# elif "The" in txt:
#     print("Yes, 'The' is present.")
# else: 
#   print("No, 'free' is present.")
  
  
"""
Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
"""
txt = "The best things in life are free!"
# print("expensive" not in txt)

# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
