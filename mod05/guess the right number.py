import random
guess_number = random.randint(1,10)
guess = (int(input("Guess the number: ")))
while guess != guess_number:
    if guess < guess_number:
        print("Too low") 
    if guess > guess_number:
        print("Too high")
    guess = (int(input("Guess the number: ")))
print("Correct")




