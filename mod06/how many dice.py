import random
dice = int(input("How many dice to roll: "))

total = 0
for n in range(dice):
    roll = random.randint(1,6)
    total = total + roll

print(f"The sum of dice is {total}")


