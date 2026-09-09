# Modify the game project program so that if the user enters an age under 12, the program informs them that they are a minor and shuts down. 
# Otherwise, the program greets the user, displays the main menu, and asks for commands until the user enters "lopeta".
# Add a few fictional commands that each produce a different output in the console. After a command, always display the menu again.



name = input("Enter your name: ")

age = int(input("Enter your age: "))

if age < 12:

    print("You are a minor and cannot play this game.")

else:

    print(f"Welcome to The Game of Thrones, {name}, {age}")

    print("MAIN MENU:\nAttack\nDefend\nExplore\nLopeta")

    command = input("Enter command: ").lower()

    while command != "lopeta":
        if command == "attack":
            print("Attack the enemy!")
        elif command == "defend":
            print("Raise your shield!")
        elif command == "explore":
            print("Explore the King's landing")
        print("MAIN MENU:\nAttack\nDefend\nExplore\nLopeta")
        command = input("Enter command: ").lower()