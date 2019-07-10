# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player(Room):
    health = 100
    def __init__(self,name,current_location,items):
        self.name = name
        self.current_location = current_location
        self.items = items

    def __str__(self):
        print(f"{self.name} is in the {self.current_location}")