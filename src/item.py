""" 
class for items, user will be able to see their inventory
"""


class Item:
    def __init__(self,name, description):
        self.name = name
        self.description = description 

    def pick_up(self):
        print(f"{self.name} was just picked up")

    def drop_it(self):
        print(f"{self.name} was just dropped")