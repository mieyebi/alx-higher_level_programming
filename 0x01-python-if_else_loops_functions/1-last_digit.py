#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0 and number < 10:
    last_digit = number
elif (number >= 10 or number < 100) or (number <= -10 or number > -100):
    last_digit = number % 10
elif (number >= 100 or number < 1000) or (number <= -100 or number > -1000):
    last_digit = number % 100
elif (number >= 1000 and number < 10000) or (number <= -1000 and number > -10000):
    last_digit = number % 1000

if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))
