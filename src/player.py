# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    health = 100
    def __init__(self,name,current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    # def __str__(self):
    #     print(f"{self.name} is in the {self.current_location}")
