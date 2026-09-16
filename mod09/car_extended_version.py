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