# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, inventory = []):
        self.name = name
        self.location = location
        self.inventory = inventory

    def move(self, direction):
        invalid = "There is nothing in that direction, please go another way."
        if direction == 'n':
            if self.location.n_to:
               self.location = self.location.n_to
            else:
                print(invalid)
        elif direction == 's':
            if self.location.s_to:
               self.location = self.location.s_to
            else:
                print(invalid)
        elif direction == 'e':
            if self.location.e_to:
               self.location = self.location.e_to
            else:
                print(invalid)
        elif direction == 'w':
            if self.location.w_to:
               self.location = self.location.w_to
            else:
                print(invalid)

    def get_item(self, item):
        self.inventory.append(item)
        self.inventory.sort()

    def list_inventory(self):
        print("Your Inventory:")
        for i, item in enumerate(self.inventory):
            print(f"{i+1}. {item}")

    def remove_item(self, item):
        self.inventory.remove(item)
        self.inventory.sort()
