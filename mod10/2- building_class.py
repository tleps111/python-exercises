# Extend the previous program by creating a Building class. 
# The initializer parameters for the class are the numbers of the bottom and top floors 
# and the number of elevators in the building. When a building is created, the building creates the required number of elevators. 
# The list of elevators is stored as a property of the building. Write a method called run_elevator that accepts the number of the 
# elevator and the destination floor as its parameters. In the main program, 
# write the statements for creating a new building and running the elevators of the building.

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        #move elevator 1 up floor
        self.current += 1
        print(f"Elevator is at floor {self.current}")
        
    def floor_down(self):
        #move elevator 1 down floor
        self.current -= 1
        print(f"Elevator is at floor {self.current}")

    def go_to_floor(self, floor):
        while self.current != floor:
            if self.current > floor:
                self.floor_down()
            else:
                self.floor_up()


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.elevators = []

        for i in range(number_of_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_number):
        elevator = self.elevators[elevator_number -1]
        elevator.go_to_floor(destination_number)

        
building = Building(1, 10, 2)
building.run_elevator(1,8)
building.run_elevator(2,5)




