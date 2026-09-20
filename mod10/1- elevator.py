# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. 
# The elevator has methods go_to_floor, floor_up and floor_down. 
# A new elevator is always at the bottom floor. If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods 
# as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell what floor the elevator is after each move. 
# Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.


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
        #moves elevator to target floor
        #using floor up and floor down

e = Elevator(1,10)
e.go_to_floor(5)
e.go_to_floor(1)

