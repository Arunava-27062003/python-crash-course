"""
Working with Part of a List

"""

"""
# Slicing a List
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']

team = ['team 1', 'team 2']

print(players[0:3]) # start at index 0 and stop at index 3 (not including index 3)

print(players[1:4]) # start at index 1 and stop at index 4 (not including index 4)

print(players[:4]) # start at the beginning of the list

print(players[2:]) # start at index 2 and continue to the end of the list

print(players[-3:]) # start at the third-last item and continue to the end of the list

print(team[-1:])

"""looping through a slice"""

print("First Three players in my team")
for player in players[:3]:
    print(player.title())
