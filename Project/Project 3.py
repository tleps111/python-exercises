# Continue developing the game project: Create a separate function for each main menu function (at least three), which is executed when the user selects that function.
    # One function must ask the user for information (e.g. an item) that is added to a list variable.
    # Another function must print the contents of the list to the user.
    # The other functions can be designed and implemented freely.


inventory = []

def item():
    item = input("What item did you find? ")
    inventory.append(item)

def show_inventory():
    print(inventory)

def explore():
    print("Explore the King's landing")
    item()

def attack():
    print("Attack the enemy!")

def defend():
    print("Raise your shield!")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age < 12:
    print("You are a minor and cannot play this game.")
else: 
    print(f"Welcome to The Game of Thrones, {name}, {age}")
    print("MAIN MENU:\nAttack\nDefend\nExplore\nInventory\nLopeta")
    command = input("Enter command: ").lower()
    while command != "lopeta":
        if command == "attack":
            attack()
        elif command == "defend":
            defend()
        elif command == "explore":
            explore()
        elif command == "inventory":
            show_inventory()   
        print("MAIN MENU:\nAttack\nDefend\nExplore\nInventory\nLopeta")
        command = input("Enter command: ").lower()
