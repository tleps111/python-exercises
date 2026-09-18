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
        #moves elebvator to target floor
        #using floor up and floor down

e = Elevator(1,10)
e.go_to_floor(5)


