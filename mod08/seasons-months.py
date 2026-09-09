# Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). 
# Save the seasons as strings into a tuple in your program. 
# We can define each season to last three months, December being the first month of winter.

seasons = ("spring","summer","autumn","winter")
month_number = int(input("Enter the month number: "))

if month_number == 12 or month_number == 1 or month_number == 2: 
    print(seasons[3])

elif month_number == 3 or month_number == 4 or month_number == 5: 
    print(seasons[0])

elif month_number == 6 or month_number == 7 or month_number == 8: 
    print(seasons[1])

elif month_number == 9 or month_number == 10 or month_number == 11: 
    print(seasons[2])



