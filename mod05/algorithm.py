import random
points = int(input("Enter the number of random points: "))
inside = 0
counter = 0

while counter < points:
    x = random.randint(-100,100) / 100
    y = random.randint(-100,100) / 100
    if x**2 + y**2 < 1:
        inside = inside + 1
    counter = counter + 1

pi = 4 * inside / points 
print("Approximation of pi:", pi)
