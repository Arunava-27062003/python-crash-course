"""The if-elif-else Chain"""

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


"""Using Multiple elif Blocks"""

age_1 = 20

if age_1 < 4:
    price = 0
elif age_1 < 18:
    price = 25
elif age_1 < 65:
    price = 40
else:
    price = 20


print(f"Your admission cost is ${price}.")

"""
# Omitting the else Block
## Python does not require an else block at the end of an if-elif chain. Sometimes, an
else block is useful. Other times, it’s clearer to use an additional elif statement that
catches the specific condition of interest:
"""

age_2 = 70

if age_2 < 4:
    price_1 = 0
elif age_2 < 18:
    price_1 = 25
elif age_2 < 65:
    price_1 = 40
elif age_2 >= 65:
    price_1 = 20


print(f"Your admission cost is ${price_1}.")