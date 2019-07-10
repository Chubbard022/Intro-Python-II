# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player(Room):
    health = 100
    def __init__(self,name,current_location):
        self.name = name
        self.current_location = current_location
