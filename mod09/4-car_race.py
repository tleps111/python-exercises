# Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the main program, create a list that consists of 10 car objects created using a loop. 
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: “ABC-1”, “ABC-2” and so on. Now the race begins. 
# One per every hour of the race, the following operations are performed:
    # The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accelerate method.
    # Each car is made to drive for one hour. This is done with the drive method.
    # The race continues until one of the cars has advanced at least 10,000 kilometers. 
    # Finally, the properties of each car are printed out formatted into a clear table.

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate (self, speed_change):
        self.current_speed = self.current_speed + speed_change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, drive_hours):
        distance = self.current_speed * drive_hours
        self.travelled_distance = self.travelled_distance + distance


import random
cars = []
for i in range(10):
    max_speed = random.randint(100,200)
    registration_number = f"ABC-{i+1}"
    car = Car(registration_number, max_speed)
    cars.append(car)

race_finished = False 

while race_finished == False:
    for car in cars: 
        car.accelerate(random.randint(-10,15))
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True
        

print(f"{'Registration':<15}{'Max Speed':<12}{'Current Speed':<16}{'Distance':<10}")
print("-" * 53)

for car in cars: 
    print(f"{car.registration_number:<15}{car.max_speed:<12}{car.current_speed:<16}{car.travelled_distance:<10}")