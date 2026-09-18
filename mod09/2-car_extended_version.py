# Extend the program by adding an accelerate method into the new class. The method should receive the change of speed (km/h) as a parameter. 
# If the change is negative, the car reduces speed. The method must change the value of the speed property of the object. 
# The speed of the car must stay below the set maximum and cannot be less than zero. Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. 
# Then print out the current speed of the car. 
# Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed. The travelled distance does not have to be updated yet.




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

car1 = (Car("ABC-123", 142))

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print(f"Current speed: {car1.current_speed} km/h")

car1.accelerate(-200)

print(f"Final speeed: {car1.current_speed} km/h")