"""
Tuples

# An immutable list is called a tuple.
"""

"""
A tuple looks just like a list, except you use parentheses instead of square brackets.
Once you define a tuple, you can access individual elements by using each item’s index,
just as you would for a list.

For example, if we have a rectangle that should always be a certain size, we can
ensure that its size doesn’t change by putting the dimensions into a tuple:

"""

dimensions = (200, 50)

"""
dimensions[0] = 250 # ❌
"""

print(dimensions)

"""
Tuples are technically defined by the presence of a comma; the parentheses
make them look neater and more readable. If you want to define a tuple with
one element, you need to include a trailing comma:
"""
my_t = (3,)

"""Looping Through All Values in a Tuple"""
for dimension in dimensions:
    print(dimension)

"""Writing Over a Tuple"""

"""
The first four lines define the original tuple and print the initial dimensions. We then
associate a new tuple with the variable dimensions, and print the new values. Python
doesn’t raise any errors this time, because reassigning a variable is valid:
"""

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)


dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)