# Store the player's information and actions.
class Player:
    # Set the player's starting name, location, health and inventory. 
    def __init__(self, name, location):
        self.name = name
        self.items = []
        self.location = location
        self.health = 100
        self.sacred_potions = 0

    # Update the player's current location.
    def move(self, destination):
        self.location = destination

    # Collect the item in the current room and update the inventory. 
    def collect_item(self):
        if self.location.item is not None:
            item = self.location.item
            self.items.append(item)
            self.location.item = None

            if item.name.startswith("Sacred Potion"):
                self.sacred_potions += 1
                print("You collected a sacred potion.")
                print(f"Sacred potions: {self.sacred_potions}/12")
            else:
                print(f"You collected {item.name}.")
        else:
            print("There is nothing to collect here.")

    # Use a Healing Potion to restore health and remove it from inventory.
    def use_healing_potion(self):
        for item in self.items:
            if item.name == "Healing Potion":
                if self.health == 100:
                    print("Your health is already full.")
                    return

                self.health += 30

                if self.health > 100:
                    self.health = 100

                self.items.remove(item)
                print("You used a Healing Potion.")
                print("Your health:", self.health)
                return

        print("You don't have a Healing Potion")

            
      