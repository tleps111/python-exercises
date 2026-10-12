# PROJECT  - THE GAME (OF THRONES)
Gökhan Korkmaz

# 1. Starting the Programming Project Assignment
The seperate folder and the readme file for the project are created. Name of the game as heading and my name below it are added.
I also created the program that asks for the player’s name and age, stores them in variables, and prints them to the console.

# 2. Main Menu
It is executed that if the user enters an age under 12, the program informs them that they are a minor and it shuts down. Otherwise if the user is of the age, the program greets the user and displays the main menu and asks for commands until the user enters "lopeta" command.
Commands are:  Attack, Defend, Explore, Lopeta

# 3. Main Menu Functions and “Inventory”
It is added that the game has separate functions for the main menu commands. The user can explore King's Landing and find items, which are added to the inventory. The user can also check the items in the inventory.
Functions are: Attack, Defend, Explore, Inventory 

# 4. Organize the Structure and Introduce Objects

## Structure:

The project is organized into separate Python modules inside the game package.

    - main.py - Creates the game objects and runs the main menu.
    - game/__init__.py - Marks the game folder as a Python package.
    - game/item.py - Contains the Item class.
    - game/room.py - Contains the Room class.
    - game/player.py - Contains the Player class. 

## Classes 

    - Item: stores the name and weight of the item

    - Room: stores the room's name and the item located in it.

    - Player: stores the player's name, inventory and current location. It also contains methods for moving between rooms and collecting items. 

## Functionality: 

The program creates a player named Tortan, two rooms, a sword and a healing potion

The main menu allows the player to move between Vormaki and the Obsidian Throne, collect an item  in the current room, view the inventory and weights of items, quit the program. 

The program has been tested to verify that movement, collecting items and displaying the inventory work correctly.


# 5. File Handling
This project reads the introduction and instructions from text files and saves and loads game progress using JSON.

    - main.py: runs the game.
    - intro.txt: introduction
    - instructions.txt: game instructions
    - save.json: saved game state
    - game/: contains the Player, Room and Item classes

Features: moving between rooms, collecting items, viewing inventory, saving and loading progress and handling missing save files. 



