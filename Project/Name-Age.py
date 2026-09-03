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
