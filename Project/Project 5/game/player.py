class Player:
    def __init__(self, name, location):
        self.name = name
        self.items = []
        self.location = location

    def move(self, destination):
        self.location = destination

    def collect_item(self):
        if self.location.item is not None:
            item = self.location.item
            self.items.append(item)
            self.location.item = None
            print(f"You collected {item.name}.")
        else:
            print("There is nothing to collect here.")
