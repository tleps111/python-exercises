age = int(input("Enter age: "))
if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))
if (age >= 18 or age >= 15 and weight >= 55):
    print("The medicine can be used.")
else: 
    print("The medicine cannot be used.")