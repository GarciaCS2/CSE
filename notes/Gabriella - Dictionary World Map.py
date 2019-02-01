player_name = "Player"
world_map = {
    "R19A": {
        'NAME': "Mr. Wiebe's Room",
        'DESCRIPTION': "This is the classroom you are in right now. "
                       "There are two doors on the north wall.",
        'PATHS': {
            'NORTH': "PARKING_LOT"

        }

    },

    "PARKING_LOT": {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "There are a couple cars parked here.",
        'PATHS': {
            'SOUTH': "R19A",
            'WEST': "CAR",
            'NORTH': "SIDEWALK"
        }
    },

    "CAR": {
        'NAME': "Your Cool Red Car.",
        'DESCRIPTION': "This car is the one you used to drive here.",
        'PATHS': {
            'EAST': "PARKING_LOT"
        }
    },
    "SIDEWALK": {
        'NAME': "The Sidewalk",
        'DESCRIPTION': "Right next to the Parking Lot. ",
        'PATHS': {
            'SOUTH': "PARKING_LOT",
            'WEST': "OVER_THERE",
            'NORTH': "STREET_1",
            'EAST': "VOIDSPACE_RIGHT"

        }
    },
    "VOIDSPACE_RIGHT": {
        'NAME': "VOIDSPACE",
        'DESCRIPTION': "You stand on nothing, and yet nothing is the void to the right of the street.",
        'PATHS': {
            'SOUTH': "VOIDSPACE_CORNER",
            'WEST': "STREET_1",
            'EAST': "VOIDSPACE_RIGHT"

        }
    },

    "VOIDSPACE_CORNER": {
        'NAME': "VOIDSPACE",
        'DESCRIPTION': "You stand on nothing, and yet nothing is the void to lower right of the world",
        'PATHS': {
            'NORTH': "VOIDSPACE_RIGHT",
            'WEST': "VOIDSPACE_LOWER",
            'EAST': "VOIDSPACE_CORNER",
            'SOUTH': "VOIDSPACE_CORNER"

        }
    },

    "VOIDSPACE_LOWER": {
        'NAME': "VOIDSPACE",
        'DESCRIPTION': "You stand on nothing, and yet nothing is the void to the south of over there.",
        'PATHS': {
            'NORTH': "OVER_THERE",
            'WEST': "VOIDSPACE_ROOM_A",
            'EAST': "VOIDSPACE_CORNER",
            'SOUTH': "VOIDSPACE_LOWER"

        }
    },

    "VOIDSPACE_ROOM_A": {
        'NAME': "VOIDSPACE_ROOM",
        'DESCRIPTION': "A comfy little room of nothingness...",
        'PATHS': {
            'NORTH': "VOIDSPACE_ROOM_B",
            'EAST': "VOIDSPACE_LOWER",
        }
    },

    "VOIDSPACE_ROOM_B": {
        'NAME': "VOIDSPACE_ROOM",
        'DESCRIPTION': "A comfy little room of nothingness....",
        'PATHS': {
            'SOUTH': "VOIDSPACE_ROOM_A",
            'EAST': "VOIDSPACE_RIGHT",
        }
    },

    "STREET_1": {
        'NAME': "Street (Right)",
        'DESCRIPTION': "Cars drive here, except there are no cars right now.",
        'PATHS': {
            'SOUTH': "SIDEWALK",
            'WEST': "STREET_2",
            'NORTH': "SIDEWALK_B1",
            'EAST': "VOIDSPACE_RIGHT"

        }
    },

    "OVER_THERE": {
        'NAME': "Over Here",
        'DESCRIPTION': "Still the Sidewalk, but over here. ",
        'PATHS': {
            'EAST': "SIDEWALK",
            'NORTH': "OVER_THERE",
            'SOUTH': "VOIDSPACE_LOWER",
            'WEST': "TRAPDOOR"
        }
    },

    "TRAPDOOR": {
        'NAME': "Place with trapdoor",
        'DESCRIPTION': "There's a trapdoor on the sidewalk...",
        'PATHS': {
            'EAST': "OVER_THERE",
            'NORTH': "TRAPDOOR_DROP",
            'SOUTH': "TRAPDOOR_DROP",
            'WEST': "TRAPDOOR_DROP"
        }
    }
}


# Controller
playing = True
current_node = world_map['R19A']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN', 'LEFT', 'RIGHT']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
        print("%s left the game" % player_name)
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("(KeyError) - Can't go there.")
        pass  # This is a placeholder.

    else:
        print("Command Not Found...")
