# Write a program that asks the user for an integer and tells if the number is a prime number. 
# Prime numbers are number that are only divisible by one or the number itself.

number = int(input("Enter a number: "))

found_divisor = False 

for divisor in range(2,number):
    if number % divisor == 0:
        found_divisor = True
  
if found_divisor:
      print(f"{number} is not a prime number")
else:
       print(f"{number} is a prime number")