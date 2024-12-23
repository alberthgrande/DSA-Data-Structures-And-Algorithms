import random
# Example
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Example to check the type of variable
print(type(x))
print(type(y))
print(type(z))

print("\n")

"""
Int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
"""
print("\n")

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

"""
Float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
"""
print("\n")

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

"""
Float can also be scientific numbers with an "e" to indicate the power of 10.
"""
print("\n")

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


"""
Complex
Complex numbers are written with a "j" as the imaginary part:
"""
print("\n")

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

"""
Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:

Note: You cannot convert complex numbers into another number type.
"""
print("\n")

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x,1)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""
Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
"""
print("\n")

print(random.randrange(1,10))