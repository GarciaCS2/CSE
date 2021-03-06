import random


class Item(object):
    def __init__(self, name, description, location=None):
        self.name = name
        self.description = description
        self.location = location


class Equipment(Item):
    def __init__(self, name, description, location, weight, condition='NEW'):
        super(Equipment, self).__init__(name, description, location)
        self.weight = weight
        self.condition = condition


class Armour(Equipment):
    def __init__(self, name, description, location, weight, protection: int, material, blessing):
        super(Armour, self).__init__(name, description, location, weight)
        self.protection = protection  # This attribute follows percentages
        self.material = material
        self.blessing = blessing  # The enchantment or buff that the armour piece has.


class Headgear(Armour):
    def __init__(self, name, description, location, protection, material, blessing):
        super(Headgear, self).__init__(name, description, location, 'MODERATE', protection, material, blessing)
        self.is_a = 'HEADGEAR'


class Gelmet(Headgear):  # INSTANTIABLE Generic Helmet
    def __init__(self, location, protection, material):
        super(Gelmet, self).__init__("Generic Helmet", "Just a regular helmet", location, protection,
                                     material, None
                                     )


class Kinghelm(Headgear):  # INSTANTIABLE King's Helmet
    def __init__(self, location, imprint):
        super(Kinghelm, self).__init__("A King's Helmet", "The helmet of which a king would wear.", location, 50,
                                       'MAGIC_GOLD', 'HONOR STATUS')
        self.imprint = imprint  # Of whom's soul does this Helmet feel of?


class Torso(Armour):
    def __init__(self, name, description, location, protection, material, blessing):
        super(Torso, self).__init__(name, description, location, 'MODERATE', protection, material, blessing)
        self.is_a = 'TORSO'


class Gorso(Torso):  # INSTANTIABLE Generic Torso
    def __init__(self, location, protection, material):
        super(Gorso, self).__init__("Generic Torso Armor", "Just your everyday armor", location, protection, material,
                                    None)


class Footwear(Armour):
    def __init__(self, name, description, location, protection, material, blessing):
        super(Footwear, self).__init__(name, description, location, 'MODERATE', protection, material, blessing)
        self.is_a = 'FOOTWEAR'


class Gboots(Footwear):  # INSTANTIABLE Generic Boots
    def __init__(self, location, protection, material):
        super(Gboots, self).__init__("Generic Boots", "Just a pair of boots", location, protection, material, None)


class Pat(Equipment):  # INSTANTIABLE Pat >>> Pan or Pot
    def __init__(self, name, description, location, kind, contents='EMPTY'):
        super(Pat, self).__init__(name, description, location, 'MODERATE')
        self.kind = kind
        self.contents = contents


class Carrier(Equipment):
    def __init__(self, name, description, location, weight, kind, tag_type, contents):
        super(Carrier, self).__init__(name, description, location, weight)
        self.kind = kind
        self.owned = False
        self.owner = ""
        self.tag_type = tag_type  # If it's a drink, it's a drawn-on label. If it's a bag, it's a tag.
        self.contents = contents


class Generic(Carrier):   # INSTANTIABLE Generic Carrier Bag
    def __init__(self, name, description, location, weight, contents=None):
        super(Generic, self).__init__(name, description, location, weight, 'THINGS', 'TAG', contents)
        self.contents = [contents]


class Thermos(Carrier):   # INSTANTIABLE Thermos
    def __init__(self, location, contents, fill=0, color="purple"):
        super(Thermos, self).__init__("Thermos", "A cup meant to hold liquids, hot or cold.", location,
                                      'LIGHT', 'LIQUIDS', 'LABEL', contents)
        self.fill = fill  # %0 is Empty, %100 is Filled
        self.color = color


class Bottle(Carrier):   # INSTANTIABLE Bottle (You can throw it)
    def __init__(self, location, material, contents='WATER'):
        super(Bottle, self).__init__("Thermos", "A bottle.", location,
                                     'LIGHT', 'LIQUIDS', 'LABEL', contents)
        self.material = material  # PLASTIC OR GLASS


class Mallobarrel(Equipment):  # INSTANTIABLE Mallobarrel
    def __init__(self, location=None, max_mallows=100, marshmallows=100):
        super(Mallobarrel, self).__init__("Marshooter Barrel", "The barrel of a Rapid-Fire Marshooter gun", location,
                                          "LIGHT")
        self.marshmallows = marshmallows  # Maximum mallows you can load
        self.max_mallows = max_mallows  # Amount of marshmallows loaded

    def count_mallows(self):
        print("In this barrel is...")
        print("%s marshmallows" % self.marshmallows)
        print("This current barrel holds %s marshmallows" % self.max_mallows)


class Tool(Equipment):  # INSTANTIABLE Tool
    def __init__(self, name, description, location, material, head):
        super(Tool, self).__init__(name, description, location, 'MODERATE')
        self.material = material
        self.head = head  # Axe, Knife, Shovel, Pick-axe, Hammer
        self.is_a = 'TOOL'


class Weapon(Equipment):
    def __init__(self, name, description, location, weight, attack_power: int, reach):
        super(Weapon, self).__init__(name, description, location, weight)
        self.attack_power = attack_power
        self.range_or_reach = reach
        self.is_a = 'WEAPON'


regular_barrel = Mallobarrel()


class Marshooter(Weapon):  # INSTANTIABLE Marshmallow Shooter
    def __init__(self, location, barrel=regular_barrel):  # Trying to link mallobarrel to marshooter
        super(Marshooter, self).__init__("Rapid-Fire Marshmallow Shooter", "It's so fast, most enemies can't handle it!"
                                         "", location, 'LIGHT', 20, 'FAR')
        self.barrel = barrel


class Standard(Weapon):  # INSTANTIABLE Generic Weapon
    def __init__(self, name, description, location, kind):
        super(Standard, self).__init__(name, description, location, 'MODERATE', 70, 'DEFAULT')
        self.kind = kind  # "MELEE" or "RANGED"


class Maxe(Weapon):  # INSTANTIABLE Magical War axe (Maxe..M-axe >>> Magic-Axe)
    def __init__(self, location, imprint, curse):
        super(Maxe, self).__init__("Magical Marble War Axe", "A lovely polished war axe made of marble, purple designs "
                                                             "painted on it like a vase...and enchanted like a curse.",
                                   location, 'MODERATE', 200, 'EXTENDED')
        self.imprint = imprint  # You can claim the weapon as your own and you shall be able to summon it at will
        self.curse = curse  # You can set a curse you want to use on your enemies


class Ord(Weapon):  # INSTANTIABLE Obsidian Sword (Ord >>> Obsidian-Sword)
    def __init__(self, location, mode):
        super(Ord, self).__init__("Obsidian Sword", "A shiny black sword made of obsidian...it can either be set aflame"
                                                    " or emit a steam of which can hide you.", location, 'MODERATE',
                                  200, 'EXTENDED')
        self.mode = mode  # Fire or Steam


class Oblet(Weapon):  # INSTANTIABLE Obliteration Mallet (Oblet >>> Obliteration-mallet)
    def __init__(self, location, charge='TEDDY BEAR'):
        super(Oblet, self).__init__("Obliteration Mallet", "A mallet lined with gold. You must hit things to charge it."
                                                           "", location, 'HEAVY', 200, 'EXTENDED')
        self.charge = charge  # Level of Impact


class Sow(Weapon):  # INSTANTIABLE Sky Bow (Sow >>> Sky-Bow)
    def __init__(self, location):
        super(Sow, self).__init__("Sky Bow", "A blue bow that feels like cloud to the touch. It's string is like that "
                                             "of a harp, except it can shoot arrows made of the mist in thin air",
                                  location, 'FEATHER', 200, 'SKY')
        self.sting = True  # No string, no service.


#  Instantiated items
other_helm = Gelmet(None, 20, 'IRON')

cool_torso = Gorso(None, 20, 'IRON')

boots = Gboots(None, 5, 'LEATHER')

pan = Pat("A pan", "A regular frying pan.", None, 'PAN')

bag = Generic("Regular Bag", "A black bag...it is empty.", None, 'LIGHT')

cup = Thermos(None, None)
print(cup.description)

water_bottle = Bottle(None, "PLASTIC", "WATER")
print(water_bottle.description)

another_mallobarrel = Mallobarrel(None, 200, 100)

sword = Standard("Some sword.", "Just a generic sword thing.", "INSERT ROOM HERE", 'MELEE')

marsh = Marshooter(None, Mallobarrel(None, 100, 100))

good_sword = Ord(None, 'FIRE')

axe = Tool("Regular axe", "Just some axe.", None, 'STONE', 'AXE')

classic_sword = Standard("Classic Sword.", "Made of sword materials.", None, 'MELEE')

magic_axe = Maxe(None, None, 'BAD_LUCK')

obsidian_sword = Ord(None, 'FLAME')

obliteration_mallet = Oblet(None)

sky_bow = Sow(None)

startup_items = {
    'WEAPONS': [sword, good_sword, classic_sword, magic_axe, obsidian_sword, obliteration_mallet, sky_bow],
    'HELMETS': [other_helm],
    'TORSO PIECES': [],
    'SHOES': [boots, ]
}

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
        self.characters = []
        self.stuff = []


class Entity(object):
    def __init__(self, name):
        self.name = name


class Interactive(Entity):
    def __init__(self, name, starting_location, health: int, money: int, weapon, helmet, torso, shoes):
        super(Interactive, self).__init__(name)
        self.current_location = starting_location
        self.health = health
        self.money = money
        self.weapon = weapon
        self.helmet = helmet
        self.torso = torso
        self.shoes = shoes
        self.armor = 0
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room to see if a room exists in that direction

        :param direction: The direction that you want to move to
        :return: The Room object if it exists, or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)  # Option 1 people get to say "return"
        return globals()[name_of_room]  # Security risk

    def calculate_armor(self):
        try:
            self.armor += self.helmet.protection
        except AttributeError or TypeError:
            pass
        try:
            self.armor += self.torso.protection
        except AttributeError or TypeError:
            pass
        try:
            self.armor += self.shoes.protection
        except AttributeError or TypeError:
            pass

    def take_damage(self, damage: int, lost=0):
        self.calculate_armor()
        if self.armor > 100:
            print("%s's armor negated all the damage." % self.name)
            print("%s lost %s health" % self.name, lost)
        else:
            self.health -= (damage*self.armor)/100
            lost = damage - (damage*self.armor)/100
            print(self.name, " lost ", lost, " health")

    def attack(self, character_target):
        print("Attack! ", self.name, "hit ", character_target.name, " for ", self.weapon.attack_power, " damage.")
        character_target.take_damage(self.weapon.attack_power)


class Player(Interactive):  # ENTITY, ATTACKABLE - PLAYER
    def __init__(self, name, starting_location, health=800, money=50):
        super(Player, self).__init__(name, starting_location, health, money, None, None, None, None)


class Character(Interactive):  # ENTITY, ATTACKABLE -  NPC
    def __init__(self, name, starting_location, health, money,  weapon, helmet, torso, shoes, hostile):
        super(Character, self).__init__(name, starting_location, health, money, weapon, helmet, torso, shoes)
        self.hostile = hostile  # True or False

    def instantialize_character(self, place):
        self.name = "Jeff"
        self.current_location = place
        self.health = random.randint(500, 1000)
        self.money = random.randint(10, 700)
        self.weapon = startup_items['WEAPONS'][random.randint(0, len(startup_items['WEAPONS'])-1)]
        self.helmet = startup_items['HELMETS'][random.randint(0, len(startup_items['HELMETS'])-1)]
        self.torso = startup_items['TORSO PIECES'][random.randint(0, len(startup_items['TORSO PIECES'])-1)]
        self.shoes = startup_items['SHOES'][random.randint(0, len(startup_items['SHOES']) - 1)]


class Guide(Entity):  # ENTITY, NON-ATTACKABLE - NPC
    def __init__(self, name, alternative_species=None):
        super(Guide, self).__init__(name)
        self.anthropoid = True
        self.alternative_species = alternative_species
        self.dialogue_tree = {
        }


guide = Guide("Gabe")

R19A = Room("Mr.Weibe's Room", "The classroom you learn in. There are two doors to the north.", 'parking_lot')
R19A.stuff = [axe]
parking_lot = Room("The North Parking Lot", "There are a couple cars parked here", 'sidewalk_A1', None, 'R19A', 'car')
car = Room("Your Cool Red Car", "This is the car you drove here in.", None, 'parking_lot', None, None, None, None,
           'freeway')
freeway = Room("On the Freeway", "You drove away", None, None, None, None, None, None, None, 'friend_house', 'home',
               'car')
friend_house = Room("Your Friend's House", "You have always been welcome here. You came just in time, too. Your friend"
                                           " and their mom are baking cookies.")
home = Room("Your warm home", "You are back in the safety of your own home. You are sitting down now with a cup of"
                              " hot chocolate reading your favorite books.")
sidewalk_A1 = Room("The Sidewalk", "...Right next to the Parking Lot.", 'street_1', 'void_space_right', 'parking_lot',
                   'sidewalk_A2')
sidewalk_A1.stuff = [obliteration_mallet]
sidewalk_A2 = Room("The Sidewalk", "Still the sidewalk, but over here.", 'street_2', 'sidewalk_A1', 'void_space_lower',
                   'sidewalk_A3')
sidewalk_A3 = Room("The Sidewalk", "There's a trapdoor in the sidewalk...", 'street_3', 'sidewalk_A2', 'trapdoor_drop',
                   'trapdoor_drop', None, 'trapdoor_drop', None, None, None, None, 'trapdoor_drop')
street_1 = Room("Street", "This is the east-most side of the street. Cars should be driving here.", 'sidewalk_B1',
                'void_space_right', 'sidewalk_A1', 'street_2')
street_1.stuff = [magic_axe, other_helm]
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
M_hallway = Room("Mysterious Hallway", "This is strangely spacious for a door frame, isn't it?", 'M_darkroom')
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


player = Player("Player", R19A)  # Eligible for both option 1 and 2


# Characters
shrine_of_deanne.characters = [guide]
void_space_right.characters = [Character("Void Wreath", void_space_right, 1000, 0, None, None, None, None, False)]
# Stuff
shrine_of_deanne.stuff = [sky_bow, good_sword]
M_marble.stuff = [Gorso("Chestplate of Honors", 400, "DIAMOND"), Ord("Dark Sword of the Flames", "FLAME")]
street_2.stuff = [Marshooter("Marshmallow Shooter Edition1"), Generic("Satchel", "A large black satchel", None, "LIGHT",
                                                                      [])]
portal_hall.stuff = [Kinghelm("King's helmet", None)]

equips = [player.weapon, player.helmet, player.torso, player.shoes]
directions = ['north',  'east', 'south', 'west', 'up', 'down', 'away', 'left', 'right', 'back', 'forward']
short_directions = ['n', 'e', 's', 'w', 'u', 'd', 'ay', 'l', 'r', 'b', 'f']


def set_item_target(string, vicinity):
    thing = None
    for b in range(len(vicinity)):
        if vicinity[b] is not None:
            if vicinity[b].name.lower() in string.lower():
                thing = vicinity[b]
    return thing


def set_character_target(string, vicinity):
    who = None
    for b in range(len(vicinity)):
        if vicinity[b] is not None:
            if vicinity[b].name.lower() in string.lower():
                who = vicinity[b]
    return who


def view_multiple_fields(string, fields: []):
    thing = None
    for c in range(len(fields)):
        thing = set_item_target(string, fields[c])
    return thing


def unequip(string):
    if player.weapon is not None:
        if player.weapon.name.lower() in string.lower():
            player.inventory.append(player.weapon)
            player.weapon = None
            print("You unequipped your weapon.")
    elif player.helmet is not None:
        if player.helmet.name.lower() in string.lower():
            player.inventory.append(player.helmet)
            player.helmet = None
            print("You unequipped your headgear.")
    elif player.torso is not None:
        if player.torso.name.lower() in string.lower():
            player.inventory.append(player.torso)
            player.torso = None
            print("You unequipped your armor.")
    elif player.shoes is not None:
        if player.shoes.name.lower() in string.lower():
            player.inventory.append(player.shoes)
            player.shoes = None
            print("You unequipped your shoes.")
    else:
        print("You do not seem to have this item equipped.")


def equip(target):
    if type(target) is Weapon:
        if player.weapon is not None:
            unequip(player.weapon.name)
        player.weapon = target
        print("You now have", target.name, "equipped as your weapon.")
        if target in player.current_location.stuff:
            player.current_location.stuff.remove(target)
        else:
            player.inventory.remove(target)
    elif type(target) is Tool:
        if player.weapon is not None:
            unequip(player.weapon.name)
        player.weapon = target
        print("You now have", target.name, "equipped as your weapon.")
        if target in player.current_location.stuff:
            player.current_location.stuff.remove(target)
        else:
            player.inventory.remove(target)
    elif type(target) is Headgear:
        if player.helmet is not None:
            unequip(player.helmet.name)
        player.helmet = target
        print("You now have", target.name, "equipped as your helmet.")
        if target in player.current_location.stuff:
            player.current_location.stuff.remove(target)
        else:
            player.inventory.remove(target)
    elif type(target) is Torso:
        if player.torso is not None:
            unequip(player.torso.name)
        player.torso = target
        print("You now have", target.name, "equipped as your armor.")
        if target in player.current_location.stuff:
            player.current_location.stuff.remove(target)
        else:
            player.inventory.remove(target)
    elif type(target) is Footwear:
        if player.shoes is not None:
            unequip(player.shoes.name)
        player.shoes = target
        print("You now have ", target.name, " equipped as your shoes.")
        if target in player.current_location.stuff:
            player.current_location.stuff.remove(target)
        else:
            player.inventory.remove(target)
    else:
        print(target.name, " isn't something you can equip.")


playing = True
while playing:  # Controller
    print()
    print(player.current_location.name)
    print(player.current_location.description)
    if 2 > len(player.current_location.characters) > 0:
        print()
        print(">>>%s is here." % player.current_location.characters[0].name)
    elif len(player.current_location.characters) >= 2:
        pass
    if len(player.current_location.stuff) == 1:
        print("In this area there is a/an", player.current_location.stuff[0].name)
    elif len(player.current_location.stuff) > 1:
        things = []
        for i in range(len(player.current_location.stuff)):
            things.append(player.current_location.stuff[i].name)
        things = ", ".join(things)
        print("In this area there is %s" % things)
    else:
        pass
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit', 'goodbye']:  # QUIT GAME
        playing = False
        print("%s left the game" % player_name)
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("You can't go that way")
    elif command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions [pos]
    elif "inventory" in command.lower():
        print("Your inventory...")
        if len(player.inventory) > 1:
            inventory = []
            for i in range(len(player.inventory)):
                inventory.append(player.inventory[i].name)
            inventory = ", ".join(inventory)
            print("You have...", inventory)
        elif len(player.inventory) > 0:
            print("You have a/an", player.inventory[0].name)
        else:
            print("You have nothing.")
    elif "unequip" in command.lower() or "take off" in command.lower():
        unequip(command.lower())
    elif "pick up" in command.lower() or "take" in command.lower() or "get" in command.lower():
        item_target = set_item_target(command.lower(), player.current_location.stuff)
        if item_target is not None:
            player.inventory.append(item_target)
            player.current_location.stuff.remove(item_target)
            print("You took a thing.")
        else:
            print("There's nothing here of that name you can pick up.")
    elif "drop" in command.lower() or "leave" in command.lower():
        item_target = set_item_target(command.lower(), player.inventory)
        if item_target is not None:
            player.current_location.stuff.append(item_target)
            player.inventory.remove(item_target)
        else:
            print("There's nothing in your inventory or that name.")
    elif "examine" in command.lower() or "look at" in command.lower() or "observe" in command.lower():  # Examine
        item_target = view_multiple_fields(command.lower(), [player.inventory, player.current_location.stuff])
        if item_target is not None:
            print(item_target.name, "...")
            print(item_target.description)
        else:
            print("There doesn't seem to be anything in your inventory or this room by that name.")
    elif "equip" in command.lower() or "put on" in command.lower() or "wear" in command.lower():
        item_target = set_item_target(command.lower(), player.inventory)
        if item_target is None:
            item_target = set_item_target(command.lower(), player.current_location.stuff)
        if item_target is not None:
            equip(item_target)
        else:
            print("There doesn't seem to be anything here by that name you can equip.")
    elif "attack" in command.lower() or "hit" in command.lower():
        target = set_character_target(command.lower(), player.current_location.characters)
        player.attack(target)

    else:
        print("Command Not Found...")
    print()
    print("---" * 9)
