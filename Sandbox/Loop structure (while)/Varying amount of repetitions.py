# d stands for decimal

import random
dice1 = dice2 = rolls = 0
while (dice1 != 6 or dice2 !=6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls + 1
print(f"Rolled {rolls:d} times")