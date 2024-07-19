
import random
import time

# Constants
SUCCESS = "You win!"
FAILURE = "You lose!"
OPTIONS = {
    "mainframe": {
        "1": "Use a brute force attack",
        "2": "Use a stealth approach"
    },
    "hideout": {
        "1": "Take out the guards silently",
        "2": "Create a distraction"
    }
}

# Global variables
score = 0
rounds = 0
max_rounds = 3  # Number of rounds to play

# Function to simulate a pause with time.sleep()
def print_pause():
    time.sleep(1)

# Function to display introduction and game instructions
def intro():
    print("Welcome, Udacity Hero!")
    print("Hackers have captured hostages and are threatening to corrupt Udacity's files.")
    print("You have 3 attempts to make the right choices and succeed!")
    print()

# Function to handle player choice and outcomes
def play_game():
    global score, rounds
    intro()
    
    while rounds < max_rounds:
        print(f"\nAttempt {rounds + 1}/{max_rounds}")
        print("Do you:")
        choice = get_choice(["1. Hack into the hacker's mainframe", "2. Infiltrate the hacker's hideout", "3. Exit"])

        if choice == "1":
            hack_outcome = hack_mainframe()
            score += 10 if "rescue" in hack_outcome else -5
        elif choice == "2":
            infiltrate_outcome = infiltrate_hideout()
            score += 15 if "rescue" in infiltrate_outcome else -8
        elif choice == "3":
            print("\nThanks for playing!")
            break
        else:
            print("Invalid choice. You lose!")

        rounds += 1
        print(f"\nCurrent Score: {score}")
        print_pause()

    if rounds >= max_rounds:
        print("\nGame Over!")
        print(f"Final Score: {score}")

    play_again()

# Function to get validated player choice
def get_choice(options):
    while True:
        print("\n".join(options))
        choice = input("> ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Function for hacking the mainframe
def hack_mainframe():
    print("\nYou try to hack into the mainframe. Do you:")
    choice = get_choice([f"1. {OPTIONS['mainframe']['1']}", f"2. {OPTIONS['mainframe']['2']}"])

    if choice == "1":
        outcome = random.choice([
            "successfully bypass the security and rescue the hostages",
            "trigger an alarm and get caught by the hackers"
        ])
        print(f"\nYou {outcome}.", SUCCESS if "rescue" in outcome else FAILURE)
        return outcome
    elif choice == "2":
        outcome = random.choice([
            "infiltrate the system unnoticed and save the files",
            "get detected and locked out"
        ])
        print(f"\nYou {outcome}.", SUCCESS if "save the files" in outcome else FAILURE)
        return outcome
    else:
        print("Invalid choice. You lose!")

# Function for infiltrating the hideout
def infiltrate_hideout():
    print("\nYou infiltrate the hacker's hideout. Do you:")
    choice = get_choice([f"1. {OPTIONS['hideout']['1']}", f"2. {OPTIONS['hideout']['2']}"])

    if choice == "1":
        outcome = random.choice([
            "neutralize the guards and free the hostages",
            "get overpowered by the guards"
        ])
        print(f"\nYou {outcome}.", SUCCESS if "free the hostages" in outcome else FAILURE)
        return outcome
    elif choice == "2":
        outcome = random.choice([
            "cause chaos and rescue the hostages in the confusion",
            "get captured in the attempt"
        ])
        print(f"\nYou {outcome}.", SUCCESS if "rescue the hostages" in outcome else FAILURE)
        return outcome
    else:
        print("Invalid choice. You lose!")

# Function to ask if the player wants to play again
def play_again():
    global score, rounds
    choice = input("\nPlay again? (yes/no): ").strip().lower()
    if choice == "yes":
        score = 0
        rounds = 0
        print_pause()
        play_game()
    elif choice == "no":
        print("\nThanks for playing!")
    else:
        print("Invalid choice. Please enter yes or no.")
        play_again()

# Entry point of the game
if __name__ == "__main__":
    play_game()
