# Import the modules and classes used in the game.
import json

from game.item import Item
from game.room import Room
from game.player import Player

# Read and display the introduction from a text file.
with open("intro.txt", "r") as file:
    intro = file.read()

print(intro)

# Read and display the game instructions from a text file.
with open("instructions.txt", "r") as file:
    instructions = file.read()

print(instructions)

# Create the items that the player can collect and use. 
sword = Item("Sword", 3.0)
healing_potion = Item("Healing Potion", 0.5)


sacred_potion_1 = Item("Sacred Potion 1", 0.2)
sacred_potion_2 = Item("Sacred Potion 2", 0.2)
sacred_potion_3 = Item("Sacred Potion 3", 0.2)
sacred_potion_4 = Item("Sacred Potion 4", 0.2)
sacred_potion_5 = Item("Sacred Potion 5", 0.2)
sacred_potion_6 = Item("Sacred Potion 6", 0.2)
sacred_potion_7 = Item("Sacred Potion 7", 0.2)
sacred_potion_8 = Item("Sacred Potion 8", 0.2)
sacred_potion_9 = Item("Sacred Potion 9", 0.2)
sacred_potion_10 = Item("Sacred Potion 10", 0.2)
sacred_potion_11 = Item("Sacred Potion 11", 0.2)
sacred_potion_12 = Item("Sacred Potion 12", 0.2)

# Create the rooms and assign items to their starting locations.
vormaki = Room("Vormaki", sword)
kingdom_2 = Room("Kingdom 2", sacred_potion_1)
kingdom_3 = Room("Kingdom 3", sacred_potion_2)
kingdom_4 = Room("Kingdom 4", sacred_potion_3)
kingdom_5 = Room("Kingdom 5", sacred_potion_4)
kingdom_6 = Room("Kingdom 6", sacred_potion_5)
kingdom_7 = Room("Kingdom 7", sacred_potion_6)
kingdom_8 = Room("Kingdom 8", sacred_potion_7)

hidden_cave = Room("Hidden Cave", sacred_potion_8)
enchanted_forest = Room("Enchanted Forest", sacred_potion_9)
ancient_temple = Room("Ancient Temple", sacred_potion_10)
mountain_shrine = Room("Mountain Shrine", sacred_potion_11)
ruined_tower = Room("Ruined Tower", sacred_potion_12)

obsidian_throne = Room("Obsidian Throne", healing_potion)
wisdom_chest = Room("Chest of Wisdom", None)

# Map the item names to their objects for loading saved games.
items_by_name = {
    "Sword": sword,
    "Healing Potion": healing_potion,
    "Sacred Potion 1": sacred_potion_1,
    "Sacred Potion 2": sacred_potion_2,
    "Sacred Potion 3": sacred_potion_3,
    "Sacred Potion 4": sacred_potion_4,
    "Sacred Potion 5": sacred_potion_5,
    "Sacred Potion 6": sacred_potion_6,
    "Sacred Potion 7": sacred_potion_7,
    "Sacred Potion 8": sacred_potion_8,
    "Sacred Potion 9": sacred_potion_9,
    "Sacred Potion 10": sacred_potion_10,
    "Sacred Potion 11": sacred_potion_11,
    "Sacred Potion 12": sacred_potion_12
}

# Store the rooms in order the player visits them. 
rooms = [
    vormaki,
    kingdom_2,
    kingdom_3,
    kingdom_4,
    kingdom_5,
    kingdom_6,
    kingdom_7,
    kingdom_8,
    hidden_cave,
    enchanted_forest,
    ancient_temple,
    mountain_shrine,
    ruined_tower,
    obsidian_throne,
    wisdom_chest
]

# Handle the fight between the player and King Sepor.
def fight_sepor(player):
    sepor_health = 100

    print("\nKing Sepor challenges you!")
    print("Your health:", player.health)
    print("Sepor's health:", sepor_health)

    while player.health > 0 and sepor_health > 0:
        print("\nA. Attack")
        print("D. Defend")
        print("H. Use Healing Potion")
        
        action = input("Choose your action: ")

        if action.lower() == "a":
            sepor_health -= 25

            if sepor_health < 0:
                sepor_health = 0

            print("You attack King Sepor!")

        elif action.lower() == "d":
            player.health += 15

            if player.health > 100:
                player.health = 100

            print("You defend yourself and recover strength")

        elif action.lower() == "h":
            player.use_healing_potion()

        else:
            print("Invalid choice. Please enter A or D or H.")
            continue
       
           
        print("Your health:", player.health) 
        print("Sepor's health:", sepor_health) 

        if sepor_health > 0:
            player.health -= 20
            print("Sepor attacks you!")
            print("Your health:", player.health)

    if player.health <= 0:
        print("Game over. You have been defeated by King Sepor")
        return False

    else:
        print("You have defeated King Sepor!")
        return True
    
#Check if the player can complete the Explorer route.
def explorer_route(player):
    if player.location.name != "Chest of Wisdom":
        print("You must reach the Chest of Wisdom first.")
        return False

    if player.sacred_potions < 12:
        print("You need all 12 sacred potions to complete your quest.")
        return False

    print("You place all 12 sacred potions in the Chest of Wisdom.")
    print("The ancient magic restores peace to the eight kingdoms!")
    print("Tortan completes his quest and becomes the guardian of the realm.")
    return True

#Check if the player can complete the Diplomat route.
def diplomat_route(player):
    if player.location.name != "Obsidian Throne":
        print("You must reach the Obsidian Throne to negotiate with King Sepor.")
        return False

    if player.sacred_potions < 12:
        print("You need all 12 sacred potions as proof of your commitment to peace.")
        return False

    print("You approach King Sepor and offer a peaceful solution.")
    print("The sacred potions help break the cycle of dark magic.")
    print("Both rulers agree to end the conflict and protect their people.")
    print("Tortan helps establish peace, justice, and strong institutions.")
    print("This ending supports UN Sustainable Development Goal 16.")
    return True

# Ask for the player's name and age
name = input("\nEnter your name: ")
age = int(input("\nEnter your age: "))

# Allow only players aged 12 or older to play the game. 
if age < 12:
    print("You are a minor and cannot play this game.")
else: 
    print(f"Welcome to The Game of Thrones, {name}, {age}")
    player = Player(name, vormaki)
    loaded_game = False

    # Check whether the player wants to continue a saved game. 
    try:
        answer = input("Continue saved game? (yes/no): ").lower()

        if answer == "yes":
            with open(f"save_{name}.json", "r") as file:
                save_data = json.load(file)

            if name != save_data["player"]:
                print("The saved game belongs to a different player.")
                print("Starting a new game instead.")

            else:
                for room in rooms:
                    if room.name == save_data["room"]:
                        player.location = room

                for item_name in save_data["inventory"]:
                    player.items.append(items_by_name[item_name])

                for room in rooms:
                    item_name = save_data["room_items"][room.name]

                    if item_name is None:
                        room.item = None
                    else:
                        room.item = items_by_name[item_name]

                player.health = save_data["health"]
                player.sacred_potions = save_data["sacred_potions"]

                print(f"Your saved location: {player.location.name}")
                print(f"Welcome back, {player.name}!")
                loaded_game = True

    except FileNotFoundError:
        print("No saved game found. Starting a new game.")

    # Keep showing the main menu until player quits or completes the game. 
    while True:
        print("\nMAIN MENU")
        print("1. Move")
        print("2. Collect item")
        print("3. Inventory")
        print("4. Save game")
        print("5. Use Healing Potion")
        print("6. Fight King Sepor")
        print("7. Choose Story Route")
        print("8. Quit")

        command = input("Choose an option: ")

        # Move the player to the next room
        if command == "1":
            current_index = rooms.index(player.location)

            if current_index < len(rooms) - 1:
                player.move(rooms[current_index +1])
            else:
                player.move(rooms[0])
                
            print(f"You moved to {player.location.name}.")

        # Let the player collect an item in the current room.
        elif command == "2":
            player.collect_item()

        # Display the items in the player's inventory.
        elif command == "3":
            if len(player.items) == 0:
                print("Your inventory is empty.")
            else:
                print("Inventory:")
                for item in player.items:
                    print(f"- {item.name}, {item.weight} kg")

        # Save the player's progress to a JSON file. 
        elif command == "4":
            if not loaded_game:
                try:
                    with open(f"save_{name}.json", "r") as file:
                        json.load(file)

                    answer = input("A saved game already exists, Overwrite it? (yes/no): ").lower()

                    if answer != "yes":
                        print("Game is not saved.")
                        continue

                except FileNotFoundError:
                    pass

            save_data = {
                "player": player.name,
                "room": player.location.name,
                "inventory": [],
                "health": player.health,
                "sacred_potions": player.sacred_potions,
                "room_items": {}
            }

            for item in player.items:
                save_data["inventory"].append(item.name)

            for room in rooms:
                if room.item is None:
                    save_data["room_items"][room.name] = None

                else:
                    save_data["room_items"][room.name] = room.item.name

            with open(f"save_{name}.json", "w") as file:
                json.dump(save_data, file)

            print("Your game has been saved.")

        # Let the player use a Healing Potion.
        elif command == "5":
            player.use_healing_potion()

        # Check the requirements before starting the fight with King Sepor.
        elif command == "6":
            if player.location.name != "Obsidian Throne":
                print("You must reach the Obsidian Throne to fight King Sepor")
            
            
            elif player.sacred_potions < 12:
                print("You need all 12 sacred potions before facing King Sepor")

            elif sword not in player.items:
                print("You need the Sword before facing King Sepor.")
            
            else:
                if fight_sepor(player):
                    print("The kingdom is free from Sepor's dark magic!")
                    break

                else:
                    print("Your adventure has ended.")
                    break

        # Let the player choose one of the three story routes. 
        elif command == "7":
            print("\nCHOOSE YOUR STORY ROUTE")
            print("1. Warrior - defeat King Sepor")
            print("2. Explorer - restore peace with the sacred potions")
            print("3. Diplomat - negotiate peace with King Sepor")

            route = input("Choose a route: ")

            if route == "1":
                print("You chose the Warrior route. Use option 6 to fight King Sepor.")

            elif route == "2":
                if explorer_route(player):
                    break

            elif route == "3":
                if diplomat_route(player):
                    break

            else:
                print("Invalid route choice.")

        # End the game when the player chooses to quit. 
        elif command == "8":
            print("Thanks for playing!")
            break