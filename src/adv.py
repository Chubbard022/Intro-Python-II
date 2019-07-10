from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    player1 = Player("curtis", room["outside"],0)
    
    print(f"{player1.name} is currently in {player1.current_location.title}")
    move = input(f"{player1.name} your next move n,e,s,w and q to quit -> ")

    if move == "n":
        if player1.current_location.n_to is not None:
            north_room = player1.current_location.n_to
            player1.current_location = north_room
            continue
    elif move == "e":
        if player1.current_location.e_to is not None:
            east_room = player1.current_location.e_to
            player1.current_location = east_room
            continue
    elif move == "s":
        if player1.current_location.s_to is not None:
            south_room = player1.current_location.s_to
            player1.current_location = south_room
            continue
    elif move == "w":
        if player1.current_location.w_to is not None:
            west_room = player1.current_location.w_to
            player1.current_location = west_room
            continue
    elif move == "q":
        print("thanks for playing")
        break
    else:
        print("Wrong move, you cannot go that direction")
