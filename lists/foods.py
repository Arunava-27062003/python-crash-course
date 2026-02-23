"""Copying a List"""

my_foods = ['pizza', 'falafel', 'Carrot cake']

friend_foods = my_foods[:]

"""
# This demonstrates why we need to copy a list properly.
# If we just assign: friend_foods = my_foods
# Both variables point to the SAME list object in memory.
# Any changes to one will affect the other.

# Example of incorrect assignment (do NOT use):
# friend_foods = my_foods
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# Result: Both lists contain ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

# Solution: Use slicing to create an independent copy
friend_foods = my_foods[:]
# Now friend_foods is a separate list with the same initial values
"""

print("My favourite foods are.........")
print(my_foods)

print("My friend's favourite foods are.........")
print(friend_foods)


my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favourite foods are.........")
print(my_foods)

print("My friend's favourite foods are.........")
print(friend_foods)
