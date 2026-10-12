import json

from game.item import Item
from game.room import Room
from game.player import Player

with open("intro.txt", "r") as file:
    intro = file.read()

print(intro)

with open("instructions.txt", "r") as file:
    instructions = file.read()

print(instructions)

sword = Item("Sword", 3.0)
potion = Item("Healing Potion", 0.5)

vormaki = Room("Vormaki", sword)
obsidian_throne = Room("Obsidian Throne", potion)

player = Player("Tortan", vormaki)

try:
    if input("Continue saved game? (yes/no): ").lower() == "yes":
        with open("save.json", "r") as file:
            save_data = json.load(file)

        player.name = save_data["player"]

        if save_data["room"] == "Obsidian Throne":
            player.location = obsidian_throne

        for item_name in save_data["inventory"]:
            if item_name == "Sword":
                player.items.append(sword)
                vormaki.item = None
            elif item_name == "Healing Potion":
                player.items.append(potion)
                obsidian_throne.item = None

        print(f"Welcome back, {player.name}!")

except FileNotFoundError:
    print("No saved game found. Starting a new game.")


while True:
    print("\nMAIN MENU")
    print("1. Move")
    print("2. Collect item")
    print("3. Inventory")
    print("4. Save game")
    print("5. Quit")

    command = input("Choose an option: ")

    if command == "1":
        if player.location == vormaki:
            player.move(obsidian_throne)
        else:
            player.move(vormaki)

        print(f"You moved to {player.location.name}.")

    elif command == "2":
        player.collect_item()

    elif command == "3":
        if len(player.items) == 0:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in player.items:
                print(f"- {item.name}, {item.weight} kg")

    elif command == "4":
        save_data = {
           "player": player.name,
           "room": player.location.name,
           "inventory": []
        }

        for item in player.items:
            save_data["inventory"].append(item.name)

        with open("save.json", "w") as file:
            json.dump(save_data, file)

        print("Your game has been saved")
    
    elif command == "5":
        print("Thanks for playing!")
        break
