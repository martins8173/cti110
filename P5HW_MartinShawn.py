#Shawn Martin
#4/27/25
#P5HW
#AI assisted character creating game
import random

# Value-returning function to create a character
def create_character():
    # Create an empty dictionary for character
    character = {}
    
    # Get user inputs for the character's attributes
    character['Name'] = input("Enter character name: ")
    character['Health'] = int(input("Enter health points: "))
    character['Mana'] = int(input("Enter mana points: "))
    character['Attack'] = int(input("Enter attack points: "))
    
    # Return the character dictionary
    return character

# Non-value-returning function to display character's attributes
def display_character(character):
    print("\nCharacter Details:")
    for key, value in character.items():
        print(f"{key}: {value}")
    print("\n")

# Function to simulate an attack between two characters
def attack(attacker, defender):
    damage = random.randint(1, attacker['Attack'])  # Attack damage is random within the attack range of the attacker
    defender['Health'] -= damage  # Subtract the damage from the defender's health
    print(f"{attacker['Name']} attacks {defender['Name']} for {damage} damage!")
    
    # Check if the defender is still alive
    if defender['Health'] <= 0:
        print(f"{defender['Name']} has been defeated!\n")
    else:
        print(f"{defender['Name']} has {defender['Health']} health left.\n")

# Main game loop
def game():
    while True:
        print("Welcome to the character creation game!\n")
        
        # Create two characters
        print("Create the first character:")
        character1 = create_character()
        display_character(character1)
        
        print("Create the second character:")
        character2 = create_character()
        display_character(character2)
        
        # Attack loop
        while character1['Health'] > 0 and character2['Health'] > 0:
            print(f"Round: {character1['Name']} vs {character2['Name']}")
            
            # Player 1 attacks Player 2
            attack(character1, character2)
            
            # If Player 2 is still alive, Player 2 attacks Player 1
            if character2['Health'] > 0:
                attack(character2, character1)
        
        # Check who won
        if character1['Health'] > 0:
            print(f"{character1['Name']} wins!")
        else:
            print(f"{character2['Name']} wins!")
        
        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    game()
