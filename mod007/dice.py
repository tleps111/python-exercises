import random
# function that returns the result of a dice role 1...6
def dice_roll():
    roll = random.randint(1,6)
    # Return the generated number
    return roll

roll = dice_roll()
while roll != 6:    
    roll = dice_roll()
    print(roll)
# continue until the dice rolls a 6
   