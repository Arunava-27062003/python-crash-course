requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    

requested_toppings = ['mushrooms', 'onions', 'green peppers', 'pineapple', 'extra cheese']

print('mushrooms' in requested_topping)

print('pepperoni' in requested_topping)

"""Testing Multiple Conditions"""

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!\n")  


for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")