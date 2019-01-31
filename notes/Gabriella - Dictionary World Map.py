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

            'NORTH': "SIDEWALK"

        }
    },

    "SIDEWALK": {
        'NAME': "The Sidewalk",
        'DESCRIPTION': "Right next to the Parking Lot. ",
        'PATHS': {
            'SOUTH': "PARKING_LOT",
            'WEST': "OVER_THERE"

        }
    },

"OVER_THERE": {
        'NAME': "The Sidewalk",
        'DESCRIPTION': "Right next to the Parking Lot. ",
        'PATHS': {
            'SOUTH': "PARKING_LOT",
            'WEST': "OVER_THERE"

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
