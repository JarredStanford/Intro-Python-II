from room import Room
from player import Player
from item import Item

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

newP = Player('Addi', room["outside"])

current_room = newP.current_room

print(current_room.name)
print(current_room.description)
print(f'This room contains: {current_room.items}')

direction = input("Please enter either a direction(n, e, s, or w) or 'controls' for more options: ")

while direction != 'q':
    command = direction.split()
    if len(command) > 1:
        if command[0] == 'pickup':
            if command[1] in current_room.items:
                newP.add_item(command[1])
                current_room.remove_item(command[1])
            else:
                print("That item is not in this room.")
        if command[0] == 'drop':
            if command[1] in newP.inventory:
                newP.drop_item(command[1])
                current_room.add_item(command[1])
            else:
                print('That item is not in your inventory.')

    
    else:
        possible = ['n', 'e', 's', 'w', 'i', 'inventory', 'controls']

        if direction == 'controls':
            print("Enter add (item name) to pick up an item in a room. Enter drop (item name) to drop an item in your inventory.")
            print("Enter 'i' or 'inventory' to see you inventory.")
            pass

        if direction not in possible:
            print("This direction is not allowed!")
            pass

        if direction == 'n':
            try:
                current_room = current_room.n_to
            except:
                print('There is nothing in this direction.')
        
        if direction == 'e':
            try:
                current_room = current_room.e_to
            except:
                print('There is nothing in this direction.')
        
        if direction == 'w':
            try:
                current_room = current_room.w_to
            except:
                print('There is nothing in this direction.')

        if direction == 's':
            try:
                current_room = current_room.s_to
            except:
                print('There is nothing in this direction.')
        
        if direction == 'i':
            print(f'Your current inventory: {newP.inventory}')

    print(f'Current Room: {current_room.name}')
    print(f'Description: {current_room.description}')
    print(f'This room contains: {current_room.items}')
    
    direction = input()

print("Thanks for playing!")