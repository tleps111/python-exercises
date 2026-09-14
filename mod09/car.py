class Car:
    def __init__(self, registeration_number, max_speed, current_speed, travelled_distance):
        self.registeration_number = registeration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

car1 = (Car("Toyota", "Red", 1984))
car2 = (Car("Volkswagen", "Blue", 1980))
car3 = (Car("Volvo", "Brown", 2005))
print(f"Car1's name: {car1.brand}, Color: {car1.color}, Production year: {car1.year} ")
print(f"Car2's name: {car2.brand}, Color: {car2.color}, Production year: {car2.year} ")