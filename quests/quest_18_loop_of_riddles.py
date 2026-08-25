#!/usr/bin/python3
# Quest 18: The Loop of Riddles
secret_number = 7
guess = None
while guess != secret_number:
    guess = int(input("Guess the secret number: "))
print("You guessed it!")
