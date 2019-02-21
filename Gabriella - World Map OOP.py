player_name = "Player"


class Room(object):
    def __init__(self, name, description, north=None, east=None, south=None, west=None, up=None, down=None, away=None,
                 left=None, right=None, back=None, forward=None):
        self.name = name
        self.description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.away = away
        self.left = left
        self.right = right
        self.back = back
        self.forward = forward

    def path(self):
        if command.upper() == "NORTH":
            return self.north()
        elif command.upper() == "EAST":
            return self.east()
        elif command.upper() == "SOUTH":
            return self.south()
        elif command.upper() == "WEST":
            return self.west
        elif command.upper() == "UP":
            return self.up
        elif command.upper() == "DOWN":
            return self.down


""" # Option 1 - Define as we go
R19A = Room("Mr.Weibe's Room")
parking_lot = Room("Parking Lot", None, R19A)

R19A.north = parking_lot  # You cannot connect earlier rooms to later rooms until after the later rooms are made.
# EASIER CONTROLS, LESS LIKELY TO MAKE SPELLING MISTAKES, LONGER CODE, MORE LIKELY TO MISS A LINK 

# Option 2 - Set all at once
R19A = Room("Mr.Weibe's Room", 'parking_lot') # Uses Strings
parking_lot = Room("Parking Lot", None, "R19A")
# TAKES MORE TIME TO GO THROUGH AND CHANGE EACH NAME OR FIX MISPELLINGS """


R19A = Room("Mr.Weibe's Room", "The classroom you learn in. There are two doors to the north.", 'parking_lot')
parking_lot = Room("The North Parking Lot", "There are a couple cars parked here", 'sidewalk_A1', None, 'R19A', 'car')
car = Room("Your Cool Red Car", "This is the car you drove here in.", None, 'parking_lot', None, None, None, None,
           'freeway')
freeway = Room("On the Freeway", "You drove away", None, None, None, None, None, None, None, 'friend_house', 'home',
               'car')
friend_house = Room("Your Friend's House", "You have always been welcome here. You came just in time, too. Your friend"
                                           "and their mom are baking cookies.")
home = Room("Your warm home", "You are back in the safety of your own home. You are sitting down now with a cup of"
                              " hot chocolate reading your favorite books.")
sidewalk_A1 = Room("The Sidewalk", "...Right next to the Parking Lot.", 'street_1', 'void_space_right', 'parking_lot',
                   'sidewalk_A2')
# Put "Over There" and "Trapdoor Area" right here.

# Put the streets right here.
street_1 = Room("Street", "This is the east-most side of the street. Cars should be driving here.", 'sidewalk_B1',
                'void_space_right', 'sidewalk_A1', 'street_2')
stret_2 = Room()
"""
 
    "STREET_2": {
        'NAME': "Street (Middle)",
        'DESCRIPTION': "Cars drive here, except there are no cars right now.",
        'PATHS': {
            'SOUTH': "OVER_THERE",
            'WEST': "STREET_3",
            'NORTH': "SIDEWALK_B2",
            'EAST': "STREET_1"
        }
    },

    "STREET_3": {
        'NAME': "Street (Left)",
        'DESCRIPTION': "Cars drive here, except there are no cars right now.",
        'PATHS': {
            'SOUTH': "TRAPDOOR",
            'WEST': "STREET_3",
            'NORTH': "SIDEWALK_B3",
            'EAST': "STREET_2"

        }
    },

    "OVER_THERE": {
        'NAME': "Over Here",
        'DESCRIPTION': "Still the Sidewalk, but over here. ",
        'PATHS': {
            'EAST': "SIDEWALK",
            'NORTH': "STREET_2",
            'SOUTH': "VOID_SPACE_LOWER",
            'WEST': "TRAPDOOR"
        }
    },

"""
sidewalk_B1 = Room("The other sidewalk", "To the north of the street, north of the parking lot.", None,
                   'void_space_right', 'street_1', 'sidewalk_B2')
sidewalk_B2 = Room("The other sidewalk", "To the north is a disembodied door.", 'M_door', 'sidewalk_B1', 'street_2',
                   'sidewalk_B3')
sidewalk_B3 = Room("The other sidewalk", "To the north is an elegant field, fenced in with stone walls. An elegant "
                                         "statue towers above in the field.", 'field', 'sidewalk_B2', 'street_3')
field = Room("Inside the fenced area", "The grass beneath your feet is moist and sparkly. To the north is that statue"
                                       " of a pegasus.", 'shrine_of_deanne', 'grass_patch', 'sidewalk_B3', 'nice_view')
shrine_of_deanne = Room("Statue area", "The almighty pegasus stares to you...", None, 'M_stone', 'field', 'pond')
pond = Room("Pond and stepping stones", "There are a bunch of assorted stones resting in a pond.", None,
            'shrine_of_deanne', 'nice_view')
nice_view = Room("Nice view", "It's a nice view of the map, despite the fact that it is not up high. You gaze at the "
                              "street and the room of which you began in this world.", 'pond', 'field')
M_stone = Room("Grassy field with a stone inscribed with a message", "There is a stone that has words engraved in it, "
                                                                     "saying:'Here stood a hero destined to find the "
                                                                     "wisdom of which would unlock our free will.",
               None, None, 'grass_patch', 'shrine_of_deanne')
grass_patch = Room("Grassy field", "You gaze up at the house next to this field. This is the place where you would find"
                                   " something, but the world is not awake at the moment.", 'M_stone', None, None,
                   'field')
void_space_right = Room("VOID SPACE", "You stand on nothing, and yet nothing is the void to the right of the street.",
                        'void_space_upper_corner', 'void_space_right', 'void_space_corner', 'street_1', None, None,
                        'void')
void_space_corner = Room("VOID SPACE", "You stand on nothing, and yet nothing is the southeast of the world.",
                         'void_space_right', 'void_space_corner', 'void_space_corner', 'void_space_lower', None, None,
                         'void')
void_space_upper_corner = Room("VOID SPACE", "You stand on nothing, and yet nothing is the void to the northeast of the"
                                             " world.", 'void_space_upper_corner', 'void_space_upper_corner',
                               'void_space_right', 'void_space_room_B', 'portal_hall', None, 'void')
void_space_lower = Room("VOID SPACE", "You stand on nothing, and yet nothing is the void to the south of the south-most"
                                      " sidewalk.", 'sidewalk_A2', 'void_space_corner', 'void_space_lower',
                        'void_space_room_A', None, None, 'void')
void_space_room_A = Room("VOID SPACE ROOM", "A comfy little room of nothingness...", 'void_space_room_B',
                         'void_space_lower', None, None, None, None, 'void')
void_space_room_B = Room("VOID SPACE ROOM", "A comfy little room of nothingness....", None, 'void_space_upper_corner',
                         'void_space_room_A', None, None, None, 'void')
void = Room("VOID", "You wandered away into the deeper darkness and got lost", None, None, None, None, None, None, None,
            None, None, 'shrine_of_deanne', 'finding_your_way')
finding_your_way = Room("VOID...", "You moved forward with conviction. You feel that you are getting somewhere.", None,
                        None, None, None, None, None, None, None, None, None, 'outside')
outside = Room("Light Area", "You stepped out of the darkness into a vast landscape bathed in light. There are patches"
                             " of darkness everywhere.", None, None, None, None, None, None, None, None, None, 'R19A')


world_map = {


    "TRAPDOOR_DROP": {
        'NAME': "Trapdoor Drop room",
        'DESCRIPTION': "This is where that Trapdoor drops those who fall in. The room looks very dark.",
        'PATHS': {
            'NORTH': "M_KITCHEN",
        }
    },

    "TRAPDOOR": {
        'NAME': "Area with trapdoor",
        'DESCRIPTION': "There's a trapdoor on the sidewalk...",
        'PATHS': {
            'EAST': "OVER_THERE",
            'NORTH': "TRAPDOOR_DROP",
            'SOUTH': "TRAPDOOR_DROP",
            'WEST': "TRAPDOOR_DROP"
        },
    },

    "M_DOOR": {
        'NAME': "Mysterious Disembodied Door",
        'DESCRIPTION': "There's a door...just, there. Nothing behind it, nothing in front. Going North would mean"
                       " just walking through it.",
        'PATHS': {
            'NORTH': "M_HALLWAY",
            'SOUTH': "SIDEWALK_B2"

        },
    },

    "M_HALLWAY": {
        'NAME': "Mysterious Hallway",
        'DESCRIPTION': "This is strangely spacey for a door frame, isn't it?",
        'PATHS': {
            'NORTH': "M_DARKROOM",
            'SOUTH': "M_DOOR"
        },
    },

    "M_DARKROOM": {
        'NAME': "A dark welcome room",
        'DESCRIPTION': "Who knew there was a place through the door...",
        'PATHS': {
            'SOUTH': "M_HALLWAY",
            'NORTH': "M_CHEST_ROOM",
            'EAST': "M_BEDROOM_1",
            'WEST': "M_KITCHEN"
        },
    },

    "M_CHEST_ROOM": {
        'NAME': "Another dark room",
        'DESCRIPTION': "There's a chest here...it's locked.",
        'PATHS': {
            'SOUTH': "M_DARKROOM",
            'WEST': "BROKEN_STAIRCASE"
        },
    },

    "M_KITCHEN": {
        'NAME': "Mysterious Kitchen",
        'DESCRIPTION': "Can you cook? All the pots and pans you'll need are here.",
        'PATHS': {
            'NORTH': "BROKEN_STAIRCASE",
            'EAST': "M_DARKROOM"
        },
    },

    "BROKEN_STAIRCASE": {
        'NAME': "Staircase up",
        'DESCRIPTION': "A long time ago, the stairs collapsed...",
        'PATHS': {
            'SOUTH': "M_KITCHEN",
            'EAST': "M_CHEST_ROOM"
        },
    },

    "M_BEDROOM_1": {
        'NAME': "Someone's bedroom.",
        'DESCRIPTION': "It looks as if no one has been here in centuries",
        'PATHS': {
            'SOUTH': "M_MARBLE",
            'NORTH': "BATHROOM",
            'WEST': "M_DARKROOM"
        },
    },

    "BATHROOM": {
        'NAME': "A Bathroom",
        'DESCRIPTION': "If you need, you can wash up and use a first-aid kit that was left over.",
        'PATHS': {
            'SOUTH': "M_BEDROOM_1"
        },
    },

    "M_MARBLE": {
        'NAME': "Marble staircase",
        'DESCRIPTION': "This staircase, in contrast to the house, looks new and polished.",
        'PATHS': {
            'NORTH': "M_BEDROOM_1",
            'UP': "PORTAL_CONNECTION",
            'EAST': "PORTAL_HALL"
        },
    },

    "PORTAL_CONNECTION": {
            'NAME': "Portal room",
            'DESCRIPTION': "Beneath you is a portal. If you allow yourself to go down, you will leave this zone..."
                           "How does this fit in the house? Speaking of which, if you want to go back in the house,"
                           " you can go west.",
            'PATHS': {
                'WEST': "M_MARBLE",
                'DOWN': "PORTAL_HALL"
            }
    },

    "PORTAL_HALL": {
        'NAME': "Portals of Worlds Hall",
        'DESCRIPTION': "Portals are lined up on the walls, some have frames and others look like mirrors. "
                       "for now, this is the end of your tour. Quit to escape.",
        'PATHS': {

        }
    }

}


# Controller
playing = True
current_node = world_map['R19A']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN', 'LEFT', 'RIGHT', 'AWAY', 'BACK']
while playing:
    print(current_node.name())
    print()
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
        print("%s left the game" % player_name)
    elif command.upper() in directions:
        try:
            room_name = ['R19A'].name()
            current_node = world_map[room_name]
        except KeyError:
            print("(NO-PATH) - Can't go there.")
        pass  # This is a placeholder.

    else:
        print("Command Not Found...")
    print()
    print("---" * 9)
