class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
car1 = (Car("Toyota", "Red", 1984))
car2 = (Car("Volkswagen", "Blue", 1980))
car3 = (Car("Volvo", "Brown", 2005))
print(f"Car1's name: {car1.brand}, Color: {car1.color}, Production year: {car1.year} ")
print(f"Car2's name: {car2.brand}, Color: {car2.color}, Production year: {car2.year} ")