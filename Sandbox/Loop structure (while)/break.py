command = input("Enter command: ")
while command != "stop":
    if command == "MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
print("Execution stopped.")