def sum_of_squares(first, second):
    result = first**2 + second**2
    return result

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = sum_of_squares(number1,number2)
print(f"The sum of squares for numbers {number1:.3f} and {number2:.3f} is {result:.3f}.")