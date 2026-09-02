#!/usr/bin/env python3
# Shebang line: Tells the Linux terminal to run this script using Python 3 executable

# Function to handle game over/defeat scenarios.
# Using a function avoids repeating the loss text formatting across multiple choices.
def game_over(reason):
    print(f"\n{reason}")  # Print the specific reason why the player lost
    print("--- GAME OVER ---")  # Print the standard end-game header

# Function to handle the winning outcome when the player succeeds.
def victory():
    print("\nYou find a glowing chest filled with ancient gold and jewels!")
    print("--- VICTORY! YOU WIN! ---")

# Location function for the left path (the canyon/bridge location).
def left_path():
    print("\nYou step onto a narrow, wooden bridge hanging over a chasm.")
    
    # Get user input. .strip() removes trailing whitespace, .lower() makes it lowercase
    # to prevent matching errors if the user types "Cross" or "CROSS".
    choice = input("Do you cross carefully or turn back? (cross/back): ").strip().lower()
    
    # Evaluate decision using conditional branching
    if choice == "cross":
        victory()  # Calls victory function if player crosses
    elif choice == "back":
        start_game()  # Restarts the game from the beginning if player turns back
    else:
        # Fallback for unexpected or invalid player inputs
        print("Indecision takes too long; the bridge breaks under your feet!")
        game_over("You fell into the abyss.")

# Location function for the right path (the dragon's lair location).
def right_path():
    print("\nYou enter a dark, sleeping dragon's lair.")
    
    # Capture user choice and normalize input casing/spacing
    choice = input("Do you try to sneak past or fight? (sneak/fight): ").strip().lower()
    
    # Check choice conditions
    if choice == "sneak":
        victory()  # Sneaking past leads to victory
    elif choice == "fight":
        game_over("The dragon wakes up and turns you to ash.")  # Fighting results in defeat
    else:
        # Invalid response handling
        game_over("You froze in panic as the dragon woke up.")

# Main function representing the starting point/hub of the game.
def start_game():
    print("\n--- THE ADVENTURE BEGINS ---")
    print("You stand at a fork in a dark forest path.")
    
    # Ask the initial navigation question
    choice = input("Do you go 'left' toward the canyon or 'right' toward the cave?: ").strip().lower()
    
    # Route execution to the chosen path function
    if choice == "left":
        left_path()  # Direct player to the bridge route
    elif choice == "right":
        right_path()  # Direct player to the dragon cave route
    else:
        # Trigger defeat if user enters anything other than 'left' or 'right'
        print("Invalid choice. A wild wolf spots you while you wander aimlessly!")
        game_over("You were defeated in the woods.")

# Entry point: Execute the main function to launch the game script
start_game()
