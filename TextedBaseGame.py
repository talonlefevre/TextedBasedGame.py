# Talon LeFevre

# this imports time to add delays to output messages
import time


# main menu and instructions on game
def show_instructions():
    print("Welcome to Robber vs Homeowner!"),
    time.sleep(1)
    print("Collect 6 items to win the game, or get turned in by the Homeowner."),
    time.sleep(3)
    print("Move Commands: go North, South, East or West"),
    time.sleep(3)
    print("Type 'Quit' to end the game at any point in time."),
    time.sleep(3)
    print("Add to Inventory: get 'item name' ")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")


# displays current room player is in
def player(rooms, current_room, inventory):
    print("You are in the", current_room)
    time.sleep(0.5)
    print("Inventory:", inventory)
    if 'item' in rooms[current_room]:
        time.sleep(0.5)
        print("You see,", rooms[current_room]['item'])
    print("---------------------------")


# return to next room
def move_room(current_room, move, rooms):
    current_room = rooms[current_room][move]
    return current_room


# add an item to inventory
def add_inventory(item, inventory, rooms, current_room):
    inventory.append(item)
    del rooms[current_room]['item']
    return inventory


# list of rooms and which direction they can go and them items in each room
def main():
    rooms = {'Living Room': {'North': 'Kitchen', 'South': 'Den', 'East': 'Office', 'West': 'Master Bedroom'},
             'Kitchen': {'South': 'Living Room', 'East': 'Garage', 'West': 'Dinning Room', 'item': 'silverware'},
             'Dinning Room': {'East': 'Kitchen', 'item': 'silver candle sticks'},
             'Garage': {'West': 'Kitchen', 'item': 'homeowner'},  # villain room
             'Master Bedroom': {'East': 'Living Room', 'item': 'jewelry box'},
             'Office': {'West': 'Living Room', 'item': 'MacBook'},
             'Den': {'North': 'Living Room', 'East': 'Bedroom', 'item': 'iPad'},
             'Bedroom': {'West': 'Den', 'item': 'Xbox'}
             }

    # display instructions
    show_instructions()

    # current room player starts in
    current_room = 'Living Room'

    # list to store items collected by player
    inventory = []

    # game loop begins
    while True:
        if current_room == 'Garage':
            print("You are in", current_room)
            print("Inventory:", inventory)
            if len(inventory) != 6:
                print("You where caught! The Homeowner turned you over to the police. ")
                break
            else:
                print("Congratulations on collecting all 6 items while sneaking by the Homeowner")
                break
        else:
            # print the status of player
            player(rooms, current_room, inventory)
            # taking player input for command using split() function
            move = input("Enter your move?: ").split(' ', 1)
            # getting directions from the current_room
            current_directions = list(rooms[current_room].keys())
            if 'item' not in current_directions:
                pass
            else:
                current_directions.remove('item')
            # if user enters quit thr game will end
            if move[0] == 'quit':
                time.sleep(0.5)
                print('You have quit the game!')
                break
            if (move[0] == 'go') and (move[1] in current_directions):
                # get to next room
                next_room = move_room(current_room, move[1], rooms)
                print("You have moved to", next_room)
                current_room = next_room
            elif (move[0] == 'go') and (move[1] not in current_directions):
                time.sleep(0.5)
                print("Invalid move from " + current_room + ". Try again!")
            elif (move[0] == 'get') and ('item' not in rooms[current_room]):
                time.sleep(0.5)
                print("Sorry, this room doesn't contain any items.")
            elif (move[0] == 'get') and (move[1] == rooms[current_room]['item']):
                # add items to inventory
                inventory = add_inventory(rooms[current_room]['item'], inventory, rooms, current_room)
            elif (move[0] == 'get') and (move[1] != rooms[current_room]['item']):
                time.sleep(0.5)
                print("This room doesn't contain an item", move[1])
            else:
                time.sleep(0.5)
                print("Invalid command")
    # output message when game ends
    time.sleep(0.5)
    print("\nThanks for playing Robber vs Homeowner!")


# call on main
main()
