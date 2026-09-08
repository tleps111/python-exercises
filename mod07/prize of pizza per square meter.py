# Write a function that receives two parameters:
# the diameter of a round pizza in centimeters and the price of the pizza in euros. 
# The function calculates and returns the unit price of the pizza per square meter. 
# The main program asks the user to enter the diameter and price of two pizzas and 
# tells the user which pizza provides better value for money 
# (which of them has a lower unit price).
#  You must use the function you wrote for calculating the unit prices.

import math

def pizza_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius**2)
    uppsm= price / area 
    area = area / 10000
    return uppsm

diameter_first_pizza = float(input("Enter the diameter of the 1st pizza: "))
price_first_pizza = float(input("Enter the price of the 1st pizza: "))

diameter_second_pizza = float(input("Enter the diameter of the 2nd pizza: "))
price_second_pizza = float(input("Enter the price of the 2nd pizza: "))

uppsm1 = pizza_price(diameter_first_pizza, price_first_pizza)
uppsm2 = pizza_price(diameter_second_pizza, price_second_pizza)

if uppsm1 < uppsm2:
    print("1st pizza provides better value for money\n as its unit price is lower than the 2nd pizza")

elif uppsm2 < uppsm1:
    print("2nd pizza provides better value for money\n as its unit price is lower than the 1st pizza")

else: 
    print("Both pizza provide equal value")