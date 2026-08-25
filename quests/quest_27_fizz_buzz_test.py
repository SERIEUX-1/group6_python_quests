#!/usr/bin/python3
# Quest 27: The FizzBuzz Test
for i in range(1, 101):
    # A number divisible by both 3 and 5 is also divisible by 15
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
