import math
talent = int(input("Enter talents: "))
pound = int(input("Enter pounds: "))
lot = float(input("Enter lots: "))

kilogram = lot / 0.0133 
gram = kilogram / 1000 
pound = 425.6 * gram
talent = 8512 * gram

print(f"The weight in modern units {kilogram:.2f} kilograms and {gram:.2f} grams")
 








