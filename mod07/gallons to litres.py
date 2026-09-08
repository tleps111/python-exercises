# Write a function that gets the quantity of gasoline in American gallons and 
# returns the number converted to litres. Write a main program that asks 
# for a volume in gallons from the user and converts the value to liters. 
# The conversion must be done by using the function. Conversions continue until 
# the user inputs a negative value.

def gallons_to_litres(gallons):
    litres = gallons * 3.785
    return litres 

gallons = float(input("Enter gallons: "))
while gallons >= 0:
    print(f"{gallons_to_litres(gallons):.2f}")
    gallons = float(input("Enter gallons: "))