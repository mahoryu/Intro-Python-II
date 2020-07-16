# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, item = []):
        self.name = name
        self.description = description
        self.item = item
        self.n_to = False
        self.s_to = False
        self.e_to = False
        self.w_to = False

    def __str__(self):
        return f"{self.name}\n{self.description}"

    def remove_item(self, item):
        self.item.remove(item)
        self.item.sort()

    def list_item(self):
        for i, item in enumerate(self.item):
            print(f"{i+1}. {item}")

    def drop_item(self, item):
        self.item.remove(item)
        self.item.sort()
