cabin  = input("Enter your cabin class: ")
if cabin.lower() == "lux":
    print("Upper-deck cabin with a balcony.")
elif cabin.lower() == "a":
    print("Above the car deck, equipped with a window.")
elif cabin.lower() == "b":
    print("Windowless cabin above the car deck.")
elif cabin.lower() == "c":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")