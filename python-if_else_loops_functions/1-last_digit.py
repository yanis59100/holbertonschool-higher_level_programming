#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
count = number % 10
if count > 5:
    print(f"Last digit of {number} is {count} and is greater than 5")
elif count == 0:
    print(f"Last digit of {number} is {count} and is 0")
else:
    print(f"Last digit of {number} is {count} and is less than 6 and not 0")
