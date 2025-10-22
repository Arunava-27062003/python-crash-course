"""organizing a list"""
"""Sorting a List Permanently with the sort() Method"""

cars = ['bmw', 'audi', 'toyota', 'honda', 'subaru']

cars.sort() # sort in alphabetical order
print(cars)

cars.sort(reverse=True) # sort in reverse-alphabetical order
print(cars)

""" Note: the order of the list 'cars' is permanently changed with 'sort()' method """

"""Sorting a List Temporarily with the sorted() Function"""

new_cars = ['tata', 'suzuki', 'ferrari', 'porsche']
print("\n Temporary Sorted List of New Cars: ")
print(sorted(new_cars))
print(f"Actual new cars list {new_cars}")

"""printing a list in reverse order"""
print("New cars list in reverse order")
new_cars.reverse()
print(new_cars)

"""finding the length of a list """
print(len(cars))

"""pg 89"""