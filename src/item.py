class Item():
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __str__(self):
        return f"{self.name} - {self.description}"

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped up {self.name}")

