#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

def square_integers(int_list):
    return [num ** 2 for num in int_list]

def fizzbuzz():
    count = 0
    while count < 100:
        count += 1
        if (count % 3 == 0) and (count % 5 == 0):
            print("FizzBuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print ("Buzz")            
        else:
            print(count)
