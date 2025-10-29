motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

"""modifying elements in a list"""
motorcycles[0]='ducati'
print(motorcycles)

"""Appending elements to the end of a list"""
motorcycles.append('honda')
print(motorcycles)

new_motorcycles = []
new_motorcycles.append('tvs')
new_motorcycles.append('ktm')
new_motorcycles.append('benelli')

print(new_motorcycles)

"""inserting elements into a list"""
motorcycles.insert(1, 'enfield')
print(motorcycles)

del motorcycles[3]
print(motorcycles)

"""The pop() method removes the last item in a list, but it lets you work with that item
after removing it."""

last_owned = motorcycles.pop()
print(f"The last owned is {last_owned.title()}.")

"""Removing an item by value"""

new_list = ['apple', 'banana', 'orange', 'mango', 'pineapple']
print(new_list)
new_list.remove('orange')
print(new_list)

print(motorcycles)
print(motorcycles[-1])