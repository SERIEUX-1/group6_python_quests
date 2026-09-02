#!/usr/bin/env python3

def game_over(reason):
    print(f"\n{reason}")
    print("--- GAME OVER ---")

def victory():
    print("\nYou find a glowing chest filled with ancient gold and jewels!")
    print("--- VICTORY! YOU WIN! ---")

def left_path():
    print("\nYou step onto a narrow, wooden bridge hanging over a chasm.")
    choice = input("Do you cross carefully or turn back? (cross/back): ").strip().lower()
    
    if choice == "cross":
        victory()
    elif choice == "back":
        start_game()
    else:
        print("Indecision takes too long; the bridge breaks under your feet!")
        game_over("You fell into the abyss.")

def right_path():
    print("\nYou enter a dark, sleeping dragon's lair.")
    choice = input("Do you try to sneak past or fight? (sneak/fight): ").strip().lower()
    
    if choice == "sneak":
        victory()
    elif choice == "fight":
        game_over("The dragon wakes up and turns you to ash.")
    else:
        game_over("You froze in panic as the dragon woke up.")

def start_game():
    print("\n--- THE ADVENTURE BEGINS ---")
    print("You stand at a fork in a dark forest path.")
    choice = input("Do you go 'left' toward the canyon or 'right' toward the cave?: ").strip().lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. A wild wolf spots you while you wander aimlessly!")
        game_over("You were defeated in the woods.")

# Start the game loop
start_game()
