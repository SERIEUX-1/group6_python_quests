#!/usr/bin/env python3

# Store constant values so they are easy to update or change later
SECRET_CODE = 42
MAX_ATTEMPTS = 3

# Loop a fixed number of times matching the allowed attempt limit.
# range(1, MAX_ATTEMPTS + 1) runs for 1, 2, and 3.
for attempt in range(1, MAX_ATTEMPTS + 1):
    # Convert input to integer for mathematical comparison
    guess = int(input(f"Attempt {attempt}/{MAX_ATTEMPTS} - Guess the secret code: "))
    
    # Check if the guess matches the secret code
    if guess == SECRET_CODE:
        print(" Access Granted! Code broken.")
        # Break out of the loop immediately so remaining attempts are skipped
        break
    else:
        # Give hints/feedback based on relative value
        if guess < SECRET_CODE:
            print("Too low!")
        else:
            print("Too high!")

# The 'else' block attached to a for-loop runs ONLY if the loop completes 
# without encountering a 'break' statement (i.e., all attempts failed).
else:
    print(f"\n Lockout engaged! The code was {SECRET_CODE}.")
