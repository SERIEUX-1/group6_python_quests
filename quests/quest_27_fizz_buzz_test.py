#!/usr/bin/python3
# the above line is shebang which shows that we are going to use python3
#then the line below is for the application of loop called for loop
for i in range(1, 101):
    # A number divisible by both 3 and 5 is also divisible by 15

#that is why we took 15
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
