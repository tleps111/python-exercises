from game.item import Item
from game.room import Room
from game.player import Player

sword = Item("Sword", 3.0)
potion = Item("Healing Potion", 0.5)

vormaki = Room("Vormaki", sword)
obsidian_throne = Room("Obsidian Throne", potion)

player = Player("Tortan", vormaki)

while True:
    print("\nMAIN MENU")
    print("1. Move")
    print("2. Collect item")
    print("3. Inventory")
    print("4. Quit")

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
        print("Thanks for playing!")
        break

    else:
        print("Invalid option, try again.")

