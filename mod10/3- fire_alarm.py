# Extend the program again by adding a method fire_alarm that does not receive any parameters
#  and moves all elevators to the bottom floor. Continue the main program by 
# causing a fire alarm in your building.


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
        self.bottom_floor = bottom_floor
        self.elevators = []

        for i in range(number_of_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_number):
        elevator = self.elevators[elevator_number -1]
        elevator.go_to_floor(destination_number)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


building = Building(1, 10, 2)
building.run_elevator(1,4)
building.run_elevator(2,2)
building.fire_alarm()

