#!/usr/bin/python3
# Quest 15: The Nested Riddle
direction = input("Do you go left or right? ")
if direction == "left":
    action = input("Do you swim or wait? ")
    if action == "swim":
        print("You find a hidden treasure!")
    else:
        print("Nothing happens. You wait in vain.")
else:
    print("You wander off and get lost.")
