#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
count = random.randint(-10, 10)
if number > 5:
    print(f"Last digit of {number} is {count} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {count} and is 0")
else:
    print(f"Last digit of {number} is {count} and is less than 6 and not 0")
