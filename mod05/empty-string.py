number = input("Enter a number: ")

if number != "":
    number = int(number)
    smallest = largest = number
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        number = int(number)
        if number < smallest:
            smallest = number 
        if number > largest:
            largest = number 
    print(f"Smallest number: {smallest}, largest number: {largest}")
