# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move(self, direction):
        invalid = "There is nothing in that direction, please go another way.\n"
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
