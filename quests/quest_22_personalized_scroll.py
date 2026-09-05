#!/usr/bin/env python3
def personalized_greeting(name, quest):
    print(f"Greetings, {name}! Your quest is to {quest}. Good luck!")


user_name = input("What is your name? ")
user_quest = input("What is your quest? ")

personalized_greeting(user_name, user_quest)
