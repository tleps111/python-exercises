command = input("Enter any command: ")
while command != "stop":
    if command == "MAYDAY":
        break
    print("Execution command: " + command)
    command = input("Enter any command: ")
else:
    print("This is the execution of the else block normally.")
print("Execution stopped.")