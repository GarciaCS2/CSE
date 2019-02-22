player_name = "Player"


class Room(object):
    def __init__(self, name, description, north=None, east=None, south=None, west=None, up=None, down=None, away=None,
                 left=None, right=None, back=None, forward=None):
        self.name = name
        self.description = description
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
sidewalk_A2 = Room("The Sidewalk", "Still the sidewalk, but over here.", 'street_2', 'sidewalk_A1', 'void_space_lower',
                   'sidewalk_A3')
sidewalk_A3 = Room("The Sidewalk", "There's a trapdoor in the sidewalk...", 'street_3', 'sidewalk_A2', 'trapdoor_drop',
                   'trapdoor_drop', None, 'trapdoor_drop', None, None, None, None, 'trapdoor_drop')
street_1 = Room("Street", "This is the east-most side of the street. Cars should be driving here.", 'sidewalk_B1',
                'void_space_right', 'sidewalk_A1', 'street_2')
street_2 = Room("Street", "This is the middle of the street.", 'sidewalk_B2', 'street_1', 'sidewalk_A2', 'street_3')
street_3 = Room("Street", "This is the west-most side of the street.", 'sidewalk_B3', 'street_2', 'sidewalk_A3',
                'street_3')
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
trapdoor_drop = Room("Trapdoor Drop Room",
                     "This is where that trapdoor drops those who fall in. The room is very dark.", 'M_kitchen')
M_door = Room("Mysterious disembodied door", "It's just kind of...there. Nothing in front, nothing behind it.",
              'M_hallway', None, 'sidewalk_B2')
M_hallway = Room("Mysterious Hallway", "This is strangely spacious for a door frame, isn't it?", 'M_kitchen')
M_darkroom = Room("A dark welcome room", "Who knew there was an actual place through the door?", 'M_chest_room',
                  'M_bedroom', 'M_hallway', 'M_kitchen')
M_chest_room = Room("Another dark room", "There's a locked chest here.", None, None, 'M_darkroom', 'broken_staircase')
M_kitchen = Room("Mysterious Kitchen", "Can you cook? All the pots, pans, and ingredients you'll need are here.",
                 'broken_staircase', 'M_darkroom')
broken_staircase = Room("Staircase Up", "A long time ago, these stairs collapsed...", None, 'M_chest_room', 'M_kitchen')
M_bedroom = Room("Someone's bedroom", "IT looks as if no one has been here in centuries.", 'bathroom', 'None',
                 'M_marble', 'M_darkroom')
bathroom = Room("A bathroom.", "If you need, you can wash up and use a first-aid kit that was left over.", None, None,
                'M_bedroom')
M_marble = Room("Marble Staircase", "This staircase, in contrast to the house, looks new and polished. How strange...",
                'M_bedroom', 'portal_connection', None, None, 'portal_connection', None, None, None, None, 'M_bedroom',
                'portal_connection')
portal_connection = Room("Room with a portal", "You are standing on a giant glass portal. If you choose to go through"
                         " it, you will leave this zone...You can't come back after that.", None, None, None,
                         'M_marble', None, 'portal_hall', 'void', None, None, 'M_marble', 'portal_hall')
portal_hall = Room("Portal of Worlds Hall", "Portals, each with a different frame, are lined up on the walls. For now, "
                                            "this is the end of your tour. Quit to escape.")
