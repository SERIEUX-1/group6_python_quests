
#!/usr/bin/env python3
# Quest 24: The Master Spell
def ask_for_age():
    return int(input("Enter your age: "))
 
 
def can_they_vote(age):
    if age >= 18:
        print("You may vote!")
    else:
        print("You are too young to vote.")
 
 
age = ask_for_age()
can_they_vote(age)
