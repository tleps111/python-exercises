# Again, extend the program by adding a new drive method that receives the number of hours as a parameter. 
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time. 
# Example: The travelled distance of car object is 2000 km. 
# The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.

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


car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

car1.drive(5)

print(f"Travelled distance: {car1.travelled_distance} km")

