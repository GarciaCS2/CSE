import random


# ____________________________________________ITEM CLASSES___________________________________________________
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Equipment(Item):
    def __init__(self, name, description, weight, condition='NEW'):
        super(Equipment, self).__init__(name, description)
        self.weight = weight
        self.condition = condition


class Armour(Equipment):
    def __init__(self, name, description, weight, protection: int, material, blessing):
        super(Armour, self).__init__(name, description, weight)
        self.protection = protection  # This attribute follows percentages
        self.material = material
        self.blessing = blessing  # The enchantment or buff that the armour piece has.


class Headgear(Armour):
    def __init__(self, name, description, protection, material, blessing):
        super(Headgear, self).__init__(name, description, 'MODERATE', protection, material, blessing)



class Gelmet(Headgear):  # INSTANTIABLE Generic Helmet
    def __init__(self, protection, material):
        super(Gelmet, self).__init__("Generic Helmet", "Just a regular helmet", protection,
                                     material, None
                                     )


class Kinghelm(Headgear):  # INSTANTIABLE King's Helmet
    def __init__(self, imprint):
        super(Kinghelm, self).__init__("A King's Helmet", "The helmet of which a king would wear.", 50,
                                       'MAGIC_GOLD', 'HONOR STATUS')
        self.imprint = imprint  # Of whom's soul does this Helmet feel of?


class Torso(Armour):
    def __init__(self, name, description, protection, material, blessing):
        super(Torso, self).__init__(name, description, 'MODERATE', protection, material, blessing)
        self.is_a = 'TORSO'


class Gorso(Torso):  # INSTANTIABLE Generic Torso
    def __init__(self, protection, material):
        super(Gorso, self).__init__("Generic Torso Armor", "Just your everyday armor", protection, material,
                                    None)


class Footwear(Armour):
    def __init__(self, name, description, protection, material, blessing):
        super(Footwear, self).__init__(name, description, 'MODERATE', protection, material, blessing)
        self.is_a = 'FOOTWEAR'


class Gboots(Footwear):  # INSTANTIABLE Generic Boots
    def __init__(self, protection, material):
        super(Gboots, self).__init__("Generic Boots", "Just a pair of boots", protection, material, None)


class Pat(Equipment):  # INSTANTIABLE Pat >>> Pan or Pot
    def __init__(self, name, description, kind, contents='EMPTY'):
        super(Pat, self).__init__(name, description, 'MODERATE')
        self.kind = kind
        self.contents = contents


class Carrier(Equipment):
    def __init__(self, name, description, weight, kind, tag_type, contents: []):
        super(Carrier, self).__init__(name, description, weight)
        self.kind = kind
        self.owned = False
        self.owner = ""
        self.tag_type = tag_type  # If it's a drink, it's a drawn-on label. If it's a bag, it's a tag.
        self.contents = contents


class Generic(Carrier):   # INSTANTIABLE Generic Carrier Bag
    def __init__(self, name, description, weight, contents=None):
        super(Generic, self).__init__(name, description, weight, 'THINGS', 'TAG', contents)
        self.contents = [contents]


class Thermos(Carrier):   # INSTANTIABLE Thermos
    def __init__(self, contents, fill=0, color="purple"):
        super(Thermos, self).__init__("Thermos", "A cup meant to hold liquids, hot or cold.",
                                      'LIGHT', 'LIQUIDS', 'LABEL', contents)
        self.fill = fill  # %0 is Empty, %100 is Filled
        self.color = color


class Bottle(Carrier):   # INSTANTIABLE Bottle (You can throw it)
    def __init__(self, material, contents='WATER'):
        super(Bottle, self).__init__("Thermos", "A bottle.",
                                     'LIGHT', 'LIQUIDS', 'LABEL', contents)
        self.material = material  # PLASTIC OR GLASS


class Mallobarrel(Equipment):  # INSTANTIABLE Mallobarrel
    def __init__(self, max_mallows=100, marshmallows=100):
        super(Mallobarrel, self).__init__("Marshooter Barrel", "The barrel of a Rapid-Fire Marshooter gun",
                                          "LIGHT")
        self.marshmallows = marshmallows  # Maximum mallows you can load
        self.max_mallows = max_mallows  # Amount of marshmallows loaded

    def count_mallows(self):
        print("In this barrel is...")
        print("%s marshmallows" % self.marshmallows)
        print("This current barrel holds %s marshmallows" % self.max_mallows)


class Tool(Equipment):  # INSTANTIABLE Tool
    def __init__(self, name, description, material, head):
        super(Tool, self).__init__(name, description, 'MODERATE')
        self.material = material
        self.head = head  # Axe, Knife, Shovel, Pick-axe, Hammer


class Weapon(Equipment):
    def __init__(self, name, description, weight, attack_power: int, reach):
        super(Weapon, self).__init__(name, description, weight)
        self.attack_power = attack_power
        self.range_or_reach = reach


class Marshooter(Weapon):  # INSTANTIABLE Marshmallow Shooter
    def __init__(self, barrel=Mallobarrel()):  # Trying to link mallobarrel to marshooter
        super(Marshooter, self).__init__("Rapid-Fire Marshmallow Shooter", "It's so fast, most enemies can't handle it!"
                                         "", 'LIGHT', 20, 'FAR')
        self.barrel = barrel


class Standard(Weapon):  # INSTANTIABLE Generic Weapon
    def __init__(self, name, description, kind):
        super(Standard, self).__init__(name, description, 'MODERATE', 70, 'DEFAULT')
        self.kind = kind  # "MELEE" or "RANGED"


class Maxe(Weapon):  # INSTANTIABLE Magical War axe (Maxe..M-axe >>> Magic-Axe)
    def __init__(self, imprint, curse):
        super(Maxe, self).__init__("Magical Marble War Axe", "A lovely polished war axe made of marble, purple designs "
                                                             "painted on it like a vase...and enchanted like a curse.",
                                   'MODERATE', 200, 'EXTENDED')
        self.imprint = imprint  # You can claim the weapon as your own and you shall be able to summon it at will
        self.curse = curse  # You can set a curse you want to use on your enemies


class Ord(Weapon):  # INSTANTIABLE Obsidian Sword (Ord >>> Obsidian-Sword)
    def __init__(self, mode):
        super(Ord, self).__init__("Obsidian Sword", "A shiny black sword made of obsidian...it can either be set aflame"
                                                    " or emit a steam of which can hide you.", 'MODERATE',
                                  200, 'EXTENDED')
        self.mode = mode  # Fire or Steam


class Oblet(Weapon):  # INSTANTIABLE Obliteration Mallet (Oblet >>> Obliteration-mallet)
    def __init__(self, charge='TEDDY BEAR'):
        super(Oblet, self).__init__("Obliteration Mallet", "A mallet lined with gold. You must hit things to charge it."
                                                           "", 'HEAVY', 200, 'EXTENDED')
        self.charge = charge  # Level of Impact


class Sow(Weapon):  # INSTANTIABLE Sky Bow (Sow >>> Sky-Bow)
    def __init__(self):
        super(Sow, self).__init__("Sky Bow", "A blue bow that feels like cloud to the touch. It's string is like that "
                                             "of a harp, except it can shoot arrows made of the mist in thin air",
                                  'FEATHER', 200, 'SKY')
        self.string = True  # No string, no service.


class Money(object):
    def __init__(self, amount):
        self.amount = amount
        self.description = "Shiny gold coins of money..."
        self.name = ("%d coins of money" % amount)

# _______________________________ROOM OBJECT____________________________________________________
class Room(object):
    def __init__(self, name, morning, noon, evening, night, north=None, east=None, south=None, west=None, up=None,
                 down=None, away=None, left=None, right=None, back=None, forward=None):
        self.name = name
        self.morning_description = morning
        self.noon_description = noon
        self.evening_description = evening
        self.night_description = night
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


# ____________________________________________ENTITY and AI CLASSES_______________________________________
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
        self.attack_power = random.randint(5, 15)
        self.dead = False

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

    def take_damage(self, attacker, damage: int, lost=0):
        self.calculate_armor()
        if self.armor > 100:
            print("%s's armor negated all the damage." % self.name)
            print("%s lost %s health" % (self.name, lost))
        else:
            lost = damage - (damage*self.armor)/100
            self.health -= lost
            print(self.name, " lost ", lost, " health")
            print(self.name, "now has", self.health, "health.")

    def attack(self, character_target):
        if self.dead:
            print(self.name, "tried to attack someone, but died.")
            return
        elif character_target is None:
            print(self.name, "went to attack someone, but couldn't figure out who.")
            return
        if self.weapon is not None:
            if isinstance(self.weapon, Weapon):
                print("Attack! ", self.name, "hit ", character_target.name, " for ",
                      (self.weapon.attack_power + (self.attack_power/2)), " damage.")
                character_target.take_damage(self, (self.weapon.attack_power + (self.attack_power/2)))
            else:
                print("Attack! ", self.name, "hit ", character_target.name, " for ", (self.attack_power*(3/2)),
                      " damage.")
                character_target.take_damage(self, (self.attack_power*(3/2)))
        else:
            print("Attack! ", self.name, "hit ", character_target.name, " for ", self.attack_power, " damage.")
            character_target.take_damage(self, self.attack_power)


class Player(Interactive):  # ENTITY, ATTACKABLE - PLAYER
    def __init__(self, name, starting_location, health=800, money=50):
        super(Player, self).__init__(name, starting_location, health, money, None, None, None, None)


player = Player("Garr!", None)


class Ai(object): # Don't use this one.
    def __init__(self, brave, faction, hostile=False):
        self.hostile = hostile
        self.brave = brave
        self.faction = faction
        self.conditions = []
        self.action = None
        self.friends = []
        self.enemies = []
        self.target = None


class Traveler(Ai):  # Applicable AI
    def __init__(self, brave: bool, faction="FULL_INNOCENT"):
        super(Traveler, self).__init__(brave, faction)

    def reaction(self, infliction):
        if "UNDER_ATTACK" in infliction:
            if "UNDER_ATTACK" not in self.conditions:
                self.conditions.append("UNDER_ATTACK")
        elif "ENEMIES_GONE" in infliction:
            if "UNDER_ATTACK" in self.conditions:
                self.conditions.remove("UNDER_ATTACK")
                if "ATTACK" in self.action:
                    self.action = None
        elif "SPOTTED" in infliction:
            if "EVIL" in infliction:
                self.action = "TARGET_SEARCH EVIL"
        else:
            pass

    def behaviours(self):
        if "UNDER_ATTACK" in self.conditions:
            if self.brave:
                self.target = self.enemies[0]
                self.action = ("ATTACK %s" % self.target.name)

            else:
                self.action = "RUN"
        else:
            self.action = None


class Hostile(Ai):  # Applicable AI
    def __init__(self, faction="EVIL"):
        super(Hostile, self).__init__(True, faction, True)

    def reaction(self, infliction):
        if "UNDER_ATTACK" in infliction:
            if "UNDER_ATTACK" not in self.conditions:
                self.conditions.append("UNDER_ATTACK")
        elif "ENEMIES_GONE" in infliction:
            if "UNDER_ATTACK" in self.conditions:
                self.conditions.remove("UNDER_ATTACK")
        if "ABSENT_WEAPON" in infliction:
            if "ABSENT_WEAPON" not in self.conditions:
                self.conditions.append("ABSENT_WEAPON")
        elif "WEAPON_FOUND" in infliction:
            if "ABSENT_WEAPON" in self.conditions:
                self.conditions.remove("ABSENT_WEAPON")
        if "SPOTTED" in infliction:
            if "PURE_INNOCENT" in infliction:
                self.action = "TARGET_SEARCH PURE_INNOCENT"
        if "PLAYER_THREAT" in infliction:
            if "PLAYER_THREAT" not in self.conditions:
                self.conditions.append("PLAYER_THREAT")
        elif "PLAYER_GONE" in infliction:
            if "PLAYER_THREAT" in self.conditions:
                self.conditions.remove("PLAYER_THREAT")
        else:
            pass

    def behaviours(self):
        if "UNDER_ATTACK" in self.conditions:
            if random.randint(1, 10) < random.randint(5, 11):
                if "ABSENT_WEAPON" in self.conditions:
                    self.action = "WEAPON_SEARCH"
                else:
                    self.action = "ATTACK"
            else:
                self.action = "ATTACK"
        if "PLAYER_THREAT" in self.conditions:
            self.target = player
            if player not in self.enemies:
                self.enemies.append(player)
            self.action = "ATTACK"
        elif "PLAYER_THREAT" not in self.conditions:
            if "ATTACK" in self.action:
                self.action = None


class Character(Interactive):  # ENTITY, ATTACKABLE -  NPC
    def __init__(self, name, starting_location, health, money, ai, weapon=None, helmet=None, torso=None,
                 shoes=None):
        super(Character, self).__init__(name, starting_location, health, money, weapon, helmet, torso, shoes)
        self.ai = ai

    def death(self):
        print(self.name, "is now dead.")
        self.dead = True
        for i in range(len(self.inventory)):
            self.current_location.stuff.append(self.inventory[i])
        my_money = Money(self.money)
        my_money.name = ("%s's money (%d Coins)" % (self.name, self.money))
        self.current_location.stuff.append(my_money)
        if self.weapon is not None:
            self.current_location.stuff.append(self.weapon)
        if self.helmet is not None:
            self.current_location.stuff.append(self.helmet)
        if self.torso is not None:
            self.current_location.stuff.append(self.torso)
        if self.shoes is not None:
            self.current_location.stuff.append(self.shoes)
        if self in self.current_location.characters:
            self.current_location.characters.remove(self)

    def attack(self, character_target):
        if self.dead:
            print(self.name, "tried to attack someone, but died.")
            return
        elif character_target is None and not isinstance(self, Player):
            if len(self.ai.enemies) == 0:
                print(self.name, "went to attack their target, but they found that they didn't have one.")
                return
            else:
                self.ai.target = self.ai.enemies[0]
            if player.current_location is self.current_location and self.ai.faction == "EVIL":
                if random.randint(1, 20) > 5:
                    self.ai.target = player
            character_target = self.ai.target
            if character_target is None:
                print(self.name, "went to attack someone, but couldn't figure out who.")
                if len(self.ai.enemies) == 0:
                    self.ai.reaction("ENEMIES_GONE")
                return
        if self.weapon is not None:
            if isinstance(self.weapon, Weapon):
                print("Attack! ", self.name, "hit ", character_target.name, " for ",
                      (self.weapon.attack_power + (self.attack_power/2)), " damage.")
                character_target.take_damage(self, (self.weapon.attack_power + (self.attack_power/2)))
            else:
                print("Attack! ", self.name, "hit ", character_target.name, " for ", (self.attack_power*(3/2)),
                      " damage.")
                character_target.take_damage(self, (self.attack_power*(3/2)))
        else:
            print("Attack! ", self.name, "hit ", character_target.name, " for ", self.attack_power, " damage.")
            character_target.take_damage(self, self.attack_power)

    def take_damage(self, attacker, damage: int, lost=0):
        self.calculate_armor()
        if self.armor > 100:
            print("%s's armor negated all the damage." % self.name)
            print("%s lost %s health" % self.name, lost)
        else:
            lost = damage - (damage*self.armor)/100
            self.health -= lost
            print(self.name, " lost ", lost, " health")
            print(self.name, "now has", self.health, "health.")
            if self.health <= 0:
                self.death()
                return
        self.ai.reaction("UNDER_ATTACK by %s" % attacker.name)
        if attacker not in self.ai.enemies:
            self.ai.enemies.append(attacker)
        if attacker in self.ai.friends:
            self.ai.friends.remove(attacker)

    def react(self, sender, action):
        # There is already a self attacked reaction.
        if self.ai.target is not None and self.ai.target.dead:
            if self.ai.target in self.ai.enemies:
                self.ai.enemies.remove(self.ai.target)
            elif self.ai.target in self.ai.friends:
                self.ai.friends.remove(self.ai.target)
            if len(self.ai.enemies) == 0:
                self.ai.target = None
                if "UNDER_ATTACK" in self.ai.conditions:
                    self.ai.conditions.remove("UNDER_ATTACK")
            else:
                for i in range(len(self.ai.enemies)):
                    if self.ai.enemies[i].current_location == self.current_location:
                        self.ai.target = self.ai.enemies[i]
        if player.current_location == self.current_location and self.ai.faction == "EVIL":  # SPOTTING PLAYER
            if "PLAYER_THREAT" not in self.ai.conditions:
                print(self.name, "is evil. They have spotted you.")
                self.ai.reaction("PLAYER_THREAT")
        elif player.current_location is not self.current_location and self.ai.faction == "EVIL":
            self.ai.reaction("PLAYER_GONE")
            print(self.name, "has lost sight of you.")
        for i in range(len(self.current_location.characters)):  # SPOTTING OTHERS
            if self.current_location.characters[i] is not self:
                self.ai.reaction((self.current_location.characters[i].ai.faction, "SPOTTED"))
        for i in range(len(self.ai.enemies)):  # SEARCH ENEMIES
            threats = 0
            if self.ai.enemies[i].current_location is self.current_location:
                threats +=1
            if threats == 0:
                self.ai.reaction("ENEMIES_GONE")
            else:
                self.ai.reaction("UNDER_ATTACK")
        if "ATTACK" in action.upper():
            recieving = set_character_target(action, self.current_location.characters)
            if recieving is None:
                pass
            elif recieving is not self:
                if recieving in self.ai.enemies:
                    self.ai.friends.append(sender)
                if recieving in self.ai.friends:
                    self.ai.enemies.append(sender)
                if recieving.ai.faction == "FULL_INNOCENT":
                    self.ai.target = sender
                    if sender not in self.ai.enemies:
                        self.ai.enemies.insert(0, sender)
                    if "UNDER_ATTACK" not in self.ai.conditions:
                        self.ai.conditions.append("UNDER_ATTACK")

    def behave(self):
        self.ai.behaviours()
        if self.ai.action is None:
            return
        if "ATTACK" in self.ai.action:
            self.attack(self.ai.target)
        elif "MOVE" in self.ai.action:
            moves = ['north', 'east', 'south', 'west', 'up', 'down']
            try:
                new_room = self.find_next_room(random.choice(moves))
                self.current_location.characters.remove(self)
                self.move(new_room)
                self.current_location.characters.append(self)
                print(self.name, "moved to", self.current_location)
            except KeyError:
                try:
                    new_room = self.find_next_room(random.choice(moves))
                    self.current_location.characters.remove(self)
                    self.move(new_room)
                    self.current_location.characters.append(self)
                    print(self.name, "moved to", self.current_location)
                except KeyError:
                    try:
                        new_room = self.find_next_room(random.choice(moves))
                        self.current_location.characters.remove(self)
                        self.move(new_room)
                        self.current_location.characters.append(self)
                        print(self.name, "moved to", self.current_location)
                    except KeyError:
                        pass
        elif "RUN" in self.ai.action:
            moves = ['north', 'east', 'south', 'west', 'up', 'down']
            try:
                new_room = self.find_next_room(random.choice(moves))
                self.current_location.characters.remove(self)
                self.move(new_room)
                self.current_location.characters.append(self)
            except KeyError:
                try:
                    new_room = self.find_next_room(random.choice(moves))
                    self.current_location.characters.remove(self)
                    self.move(new_room)
                    self.current_location.characters.append(self)
                except KeyError:
                    try:
                        new_room = self.find_next_room(random.choice(moves))
                        self.current_location.characters.remove(self)
                        self.move(new_room)
                        self.current_location.characters.append(self)
                    except KeyError:
                        print(self.name, "tried to move away, but couldn't.")
        elif "SEARCH" in self.ai.action:
            if player.current_location == self.current_location:
                self.ai.target = player
            found = True
            if "WEAPON_SEARCH" in self.ai.action:
                print(self.name, "is searching for a weapon.")
                while self.weapon is None and found is not False:
                    for i in range(len(self.current_location.stuff)):
                        if isinstance(self.current_location.stuff[i], Weapon):
                            self.weapon = self.current_location.stuff[i]
                            self.current_location.stuff.remove(self.current_location.stuff[i])
                        else:
                            if random.randint(1, 10) < 3:
                                self.ai.action = "MOVE"
                            found = False
            elif "TARGET_SEARCH" in self.ai.action:
                for i in range(len(self.current_location.characters)):
                    if self.current_location.characters[i] is not self:
                        if self.current_location.characters[i].ai.faction == self.ai.action[14:]:
                            if self.current_location.characters[i] not in self.ai.enemies:
                                self.ai.enemies.append(self.current_location.characters[i])
                        elif self.current_location.characters[i].ai.faction == self.ai.faction:
                            if self.current_location.characters[i] not in self.ai.friends:
                                self.ai.friends.append(self.current_location.characters[i])


# ______________________________________________ROOMS INSTANTIATED______________________________________________________



# HOME
starting_room = Room("A Room", "A generic room. There's all kinds of stuff scattered all over the place.",
                     "A generic room. There's all kinds of stuff scattered all over the place.",
                     "A generic room. There's all kinds of stuff scattered all over the place.",
                     "A generic room. There's all kinds of stuff scattered all over the place.", None,
                     'ns_hallway_north')
ns_hallway_north = Room("Home Hallway, Northern Side",
                        "To the west is a room. The hallway leads south, flooded by morning light.",
                        "To the west is a room. The hallway leads south.",
                        "To the west is your bedroom. To the east is the livingroom.",
                        "This hallway has a door on the east side and 2 doors on the west side, one that you're "
                        "standing next to right now.", None, None, 'ns_hallway_south', 'starting_room')
ns_hallway_south = Room("Home Hallway, Southern Side", "To the west is your bedroom. To the east is the livingroom. "
                                                       "Morning light floods the hallway.",
                        "To the west is your bedroom. To the east is the livingroom.",
                        "To the west is your bedroom. To the east is the livingroom.",
                        "This hallway has 2 doors to the west side(one north and one south), and one east right next "
                        "to you.")
kitchen_west = Room("Your Kitchen, West Side.",
                    "This is your kitchen. It's a lovely kitchen. To the south is the livingroom.",
                    "This is your kitchen. It's a nice kitchen. To the south is the livingroom.",
                    "This is your kitchen. It's a cool kitchen. To the south is the livingroom.",
                    "You're in your kitchen.", None, 'kitchen_east', 'livingroom_north')
kitchen_east = Room("Your Kitchen, East Side.",
                    "This is your kitchen. It's a lovely kitchen.",
                    "This is your kitchen. It's a nice kitchen.",
                    "This is your kitchen. It's a cool kitchen.",
                    "You're in your kitchen.", None, 'kitchen_east', 'livingroom_north')
livingroom_south = Room("Your Livingroom, Southern Side", "Your livingroom is a very welcoming room. Morning light" 
                        " shines through the window. To west is a hallway, east leads to your bathroom.",
                        "Your living room is a very welcoming room. Covering the floor of this room is an ocean of "
                        "carpet, the bathroom just a small voyage east and a hallway a voyage west.",
                        "Your living room is a very comforting room. To the east is your bathroom and a hallway west.",
                        "All of the colors in your living room are now bathed in dark blue tones. Starlight shines "
                        "from the window.", 'livingroom_north', 'bathroom', None, 'ns_hallway_south')
livingroom_north = Room("Your Livingroom, Northern Side.", "Your livingroom is a very welcoming room. Morning light" 
                        " shines from the south and through the door across that hallway east.",
                        "Your living room is a very welcoming room. Covering the floor of this room is an ocean of "
                        "carpet, the exit hallway just a small voyage east.",
                        "Your living room is a very comforting room. To the east is the exit hallway.",
                        "All of the colors in your living room are now bathed in dark blue tones. Starlight shines "
                        "from the south.", 'kitchen_west', 'we_hallway')
we_hallway = Room("Doorway hallway", "The hallway connects the door to the rest of the house. There are some vivid "
                                     "paintings of your later ancestors lined across the white walls.",
                  "The hallway connects the door to the rest of the house. There are some vivid paintings lined "
                  "across the white walls.", "The hallway connects the door to the rest of the house. There are some"
                                             " paintings lined across the walls.",
                  "The hallway connects the door to the rest of the house.", None, 'patio', None, 'livingroom_north')
patio = Room("Your patio", "The fluffy morning daylight comes through your patio. The morning sunshine brings new "
                           "opportunity.", "The light continues to shine through to your patio.",
             "The light hitting your patio is starting to dim.",
             "The countless starts shimmer. The dark sky blankets the world as you stand on your patio.", None,
             'jason_rd_6down', None, 'we_hallway')
behind_home = Room("Behind Your House", "The space behind your house next to Jason Road. Your house looks lovely in the"
                                        " morning light, doesn't it?",
                   "The space behind your house next to Jason Road. Your house looks lovely, doesn't it?",
                   "The space behind your house next to Jason Road. Your house looks lovely.",
                   "The space behind your house next to Jason Road. It's a little hard to see, but you can see your "
                   "lovely home.", None, 'jason_rd_7down', None, 'around_home')
around_home = Room("Around Your House", "The space farther west from behind your house next to Jason Road. Your house "
                                        "looks lovely in the morning light, doesn't it? look at the stunning shadow it"
                                        " casts!",
                   "The space farther west from behind your house next to Jason Road. Your house looks lovely, doesn't"
                   " it? Look at the shadow it casts!",
                   "The space farther west from behind your house next to Jason Road. Your house looks lovely and casts"
                   " a shadow.",
                   "The space behind your house next to Jason Road. That shadow is hiding now.", 'ledge_next_to_home',
                   'behind_home')
ledge_next_to_home = Room("Ledge Next to Your Home",
                          "You stand on a beautiful ledge covered in grass next to your home. Morning's light reveals "
                          "a large dark tower far in the west past the ledge.",
                          "You stand on a beautiful ledge covered in grass next to your home. To the west, there is a "
                          "large dark tower, of which a large land gap is.",
                          "As you stand on the ledge next to your home, the tower you saw to your west becomes less "
                          "visible with the fading light.",
                          "You stand on the grass on the ledge next to your home. As you look about, everything far in "
                          "distance is shrouded in darkness.", None, None, 'around_home')
# DEANNE MAIN -------------
jason_rd_1up = Room("Jason Road 1-Up",
                    "The shining cobblestone path draws incomplete as the rest of the path is broken. Past that is a "
                    "statue of a pegasus.",
                    "The cobblestone path is incomplete here, stopping somewhere north. Past that is a statue of a "
                    "pegasus that seems to look to you.",
                    "You stand on a road incomplete to the north. The statue of the pegasus stares to you",
                    "That statue of the pegasus still stares at you, as if it is pleading for help.",
                    None, None, 'deanne_jason_crossroad')
deanne_jason_crossroad = Room("Deanne-Jason Crossroad",
                              "The Grand Deanne Jason-Crossroad is quite grand. It is also composed of many-much "
                              "cobblestone pieces, looking polished in the daylight",
                              "The Grand Deanne Jason-Crossroad is composed of many grand cobblestone pieces. To the "
                              "west is the Gates to Tsard.",
                              "The Grand Deanne Jason-Crossroad is the intersection of Deanne Road and Jason Road. "
                              "Going westward, you will find yourself at the Great Gates of Tsard.",
                              "Tsard is westward. The stars reveal that, and the pegasus statue to the north.",
                              'jason_rd_1up', 'deanne_3split_crossroad', 'jason_rd_1down', 'tsard_gates')
tsard_gates = Room("East Gates of the Great Tsard City", "The sun continues to shine brightly upon the gates of this "
                                                         "city, despite the city having lost its own light",
                   "Tsard's gates to the west stand between you and a once-flourishing town.",
                   "The sun has begun to set, but it may very well have already set on Great Tsard's glory.",
                   "The countless stars shed a dim light on Tsard's gates.", None, 'deanne_jason_crossroad')
deanne_3split_crossroad = Room("Deanne West-North_South Splitroad",
                               "The cobblestone of the great Deanne Splitroad is illuminated by the morning light.",
                               "You walk on a decisive cobblestone splitroad, with pretty cool grass around it.",
                               "There is an exceptional amount of cobblestone pieces in this road you tread on.",
                               "The cobblestone of the great Deanne splitroad is illuminated by the nighttime stars.",
                               'deanne_north_1far', None, 'deanne_south_1far', 'deanne_jason_crossroad')
# DEANNE SOUTH and TOWER -------------
deanne_south_1far = Room("Deanne Splitroad South 1-far", "The cobblestone path beams from the morning sunlight.",
                         "You walk on a proud cobblestone path. Next to the path on both sides is fond grass.",
                         "You walk on a proud cobblestone path, composed of pieces that in a particular way, work out.",
                         "You hear your steps on the cobblestone path. The sounds your steps make on this cobblestone "
                         "is somehow comforting.", 'deanne_3split_crossroad')
fate_tower_1_doorstep = Room("Great Shrine of Tsard", "The Great Shrine of Tsard...the morning implores you to have "
                                                      "warm memories that don't really belong to you.",
                             "The Great Shrine of Tsard...this was built in the name of Tsard.",
                             "The Great Shrine of Tsard...it too fell into darkness as Tsard fell from light.",
                             "The Former Shrine of Tsard...the night's wind brings gloomy chills that are somehow "
                             "familiar to you.", 'deanne_south_1far', None, 'fate1_large_hall')  # DOORSTEP
fate1_large_hall = Room("Tsard Shrine Large Hall", "Chairs are set aside for audiences to sit in and attend ceremonies "
                                                   "of such. There is a stage-like elevated floor to the south.",
                        "Chairs are set aside for audiences to sit in. There is a stage-like elevated floor to the "
                        "south.", "Chairs are set aside. There is a stage-like elevated floor to the south.",
                        "There is a space on the floor that seems elevated to the south.", 'fate1_elevated_floor')
fate1_elevated_floor = Room("Great Stage of Tsard", "This was the perfect place for a wedding. This is where the couple"
                                                    " would stand together. There still feels as if there is joy "
                                                    "remaining here in an otherwise dull place.",
                            "This was the perfect place for a wedding. This is where the couple would stand together. "
                            "There are staircases to the west and east.",
                            "This was the perfect place for a wedding. There are staircases to the west and east.",
                            "This was the perfect place for the wedding...", 'fate1_large_hall','fate1_staircase',
                            None, 'fate1_staircase')
fate1_staircase = Room("STAIRCASE UP.",
                       "Type 'UP' or 'FORWARD' to go upstairs. Type 'BACK' or 'DOWN' to return to the Stage.",
                       "Type 'UP' or 'FORWARD' to go upstairs. Type 'BACK' or 'DOWN' to return to the Stage.",
                       "Type 'UP' or 'FORWARD' to go upstairs. Type 'BACK' or 'DOWN' to return to the Stage.",
                       "Type 'UP' or 'FORWARD' to go upstairs. Type 'BACK' or 'DOWN' to return to the Stage.")
fate1_staircase.up = 'fate1_floor2'
fate1_staircase.forward = 'fate1_floor2'
fate1_staircase.down = 'fate1_elevated_floor'
fate1_staircase.back = 'fate1_elevated_floor'
fate1_floor2 = Room("TSARD ABANDONED SHRINE, FLOOR 2",
                    "You have to reach the third floor. (UP = Thrid floor, BACK, WEST, or EAST = staircase)",
                    "You have to reach the third floor. (UP = Thrid floor, BACK, WEST, or EAST = staircase)",
                    "You have to reach the third floor. (UP = Thrid floor, BACK, WEST, or EAST = staircase)",
                    "You have to reach the third floor. (UP = Thrid floor, BACK, WEST, or EAST = staircase)")
# NOTE: CREATE EVENT TO CREATE PASSAGE TO THIRD FLOOR
fate1_floor3 = Room("TSARD ABANDONED SHRINE, THE THIRD FLOOR", "You're at the third floor. The morning sun beams at "
                                                               "you through the towering tower window.",
                    "You're at the third floor.", "You're at the third floor.",
                    "You're at the third floor. The stars beam at you through the towering tower window.")
# NOTE: CREATE EVENT TO CREATE PASSAGE BACK TO SECOND FLOOR
# NOTE: PUT MOUNT ON THAT FLOOR!
# DEANNE NORTH -------------
deanne_north_1far = Room("Deanne Splitroad North 1-far", "The cobblestone path glows from the morning sunlight.",
                         "You walk on an unwavering cobblestone path. Next to the path on both sides is intimidating "
                         "grass.", "You walk on an unwavering cobblestone path. The path is composed of flawless "
                                   "cobblestone pieces.", "You hear your steps on the cobblestone path. Somehow, the "
                                                          "sounds of your footsteps on this cobblestone is scary.",
                         'deanne_north_2far')
deanne_north_2far = Room("Deanne Splitroad North 2-far", "The cobblestone path glows from the morning sunlight.",
                         "You walk on an unwavering cobblestone path. Next to the path on both sides is intimidating "
                         "grass.", "You walk on an unwavering cobblestone path. The path is composed of flawless "
                                   "cobblestone pieces.", "You hear your steps on the cobblestone path. Somehow, the "
                                                          "sounds of your footsteps on this cobblestone is scary.",
                         'deanne_north_3far', None, 'deanne_north_1far')
deanne_north_3far = Room("Deanne Splitroad North 3-far", "The cobblestone path glows from the morning sunlight.",
                         "You walk on an unwavering cobblestone path. Next to the path on both sides is intimidating "
                         "grass.", "You walk on an unwavering cobblestone path. The path is composed of flawless "
                                   "cobblestone pieces.", "You hear your steps on the cobblestone path. Somehow, the "
                                                          "sounds of your footsteps on this cobblestone is scary.",
                         'deanne_north_4far', None, 'deanne_north_2far')
deanne_north_4far = Room("Deanne Splitroad North 4-far", "The cobblestone path glows from the morning sunlight.",
                         "You walk on an unwavering cobblestone path. Next to the path on both sides is intimidating "
                         "grass.", "You walk on an unwavering cobblestone path. The path is composed of flawless "
                                   "cobblestone pieces.", "You hear your steps on the cobblestone path. Somehow, the "
                                                          "sounds of your footsteps on this cobblestone is scary.",
                         None, None, 'deanne_north_3far', 'fate_tower_2_doorstep')
fate_tower_2_doorstep = Room("(Almost) The Guarded Watchtower of Tsard.",
                             "The morning's light usually comforts you somehow... alas, the Fallen Watchtower sweeps "
                             "hope away.", "The Fallen Watchtower stares down at you.",
                             "The Fallen Watchtower implores that you remember chilling memories that don't belong "
                             "to you.", "Why would you come here at  n i g h t . . . ",
                             None, 'deanne_north_4far')  # DOORSTEP
fate2_door = Room("The Fallen Watchtower of Tsard", "Westward leads inside. Be careful!",
                  "Westward leads inside. Be careful!", "Westward leads inside. Be careful!",
                  "Westward leads inside. Be careful!")
# NOTE: CREATE EVENT TO OPEN DOORS
fate2_forge = Room("LEDGENDARY FORGE",
                   "Despite that the Tsard's hold on this Tower is long gone, this forge is still held in high regard "
                   "as if it were still Tsard's.",
                   "Despite that the Tsard's hold on this Tower is long gone, this forge is still held in high regard.",
                   "This forge is still held in high regard.",
                   "The lava around this great forge does not comfort you in the same way morning's light does, but "
                   "nonetheless it gives you strength.")
fate2_forge.up = 'fate2_floor1'
fate2_forge.back = 'fate2_floor1'
fate2_floor1 = Room("TSARD ABANDONED WATCHTOWER, FLOOR 1",
                    "There's tons of battle gear stored here! (UP = second floor, DOWN = Forge, BACK = back outside)",
                    "There's tons of battle gear stored here! (UP = second floor, DOWN = Forge, BACK = back outside)",
                    "There's tons of battle gear stored here! (UP = second floor, DOWN = Forge, BACK = back outside)",
                    "There's tons of battle gear stored here! (UP = second floor, DOWN = Forge, BACK = back outside)",)
fate2_floor1.up = 'fate2_floor2'
fate2_floor1.down = 'fate2_forge'
fate2_floor1.back = 'fate2_door'
fate2_floor2 = Room("TSARD ABANDONED WATCHTOWER, FLOOR 2",
                    "You must reach the third floor at all costs! (UP = third floor, DOWN = first floor)",
                    "You must reach the third floor at all costs! (UP = third floor, DOWN = first floor)",
                    "You must reach the third floor at all costs! (UP = third floor, DOWN = first floor)",
                    "You must reach the third floor at all costs! (UP = third floor, DOWN = first floor)",)
fate2_floor2.up = ''
fate2_floor2.down = 'fate2_floor1'
fate2_floor3 = Room("TSARD ABANDONED WATCHTOWER, THE THIRD FLOOR",
                    "You're at the third floor. In the center of a room is a pedestal for a sword to rest in. "
                    "The morning light watches over you.",
                    "You're at the third floor. In the center of a room is a pedestal for a sword to rest in.",
                    "You're at the third floor. In the center of a room is a pedestal for a sword to rest in.",
                    "You're at the third floor. In the center of a room is a pedestal for a sword to rest in. The "
                    "starlight watches over you.")
fate2_floor3.up = 'fate2_top'
fate2_floor3.down = 'fate2_floor2'
fate2_floor3.back = 'fate2_floor2'
fate2_top = Room("The Top of the Tower",
                 "The rising sun looks quite beautiful up here. Here you can see all of Tsard city.",
                 "You stand at the top of the Tower. The greatest bliss is found when one marches through fear.",
                 "You stand at the top of the Tower. There is a nice breeze.",
                 "The setting sun looks quite beautiful up here. Here you can see all of Tsard city, and your home.")
fate2_top.down = 'fate2_floor3'
fate2_top.back = 'fate2_floor3'
# JASONS A -------------
jason_rd_1down = Room("Jason Road 1-Down", "The cobblestone path shines as if it were polished by the sunlight.",
                      "You walk on a sturdy cobblestone path. Next to the path on both sides is stunning grass.",
                      "You walk on a sturdy cobblestone path. It seems to be composed of quite a bit of cobblestone "
                      "pieces.", "You hear your steps on the cobblestone path. You can barely see all the pieces that"
                                 " make up the path, but you know the number of pieces is no match for the billions of"
                                 " stars in the sky.", 'deanne_jason_crossroad', None, 'jason_rd_2down')
jason_rd_2down = Room("Jason Road 2-Down", "The cobblestone path shines as if it were polished by the sunlight.",
                      "You walk on a sturdy cobblestone path. Next to the path on both sides is great grass.",
                      "You walk on a sturdy cobblestone path. It seems to be composed of quite a bit of cobblestone "
                      "pieces.", "You hear your steps on the cobblestone path. You can barely see all the pieces that"
                                 " make up the path, but you know the number of pieces is no match for the billions of"
                                 " stars in the sky.", 'jason_rd_1down', None, 'jason_rd_3down', None)
jason_rd_3down = Room("Jason Road 3-Down", "The cobblestone path shines as if it were polished by the sunlight.",
                      "You walk on a sturdy cobblestone path. Next to the path on both sides is nice grass.",
                      "You walk on a sturdy cobblestone path. It seems to be composed of quite a bit of cobblestone "
                      "pieces.", "You hear your steps on the cobblestone path. You can barely see all the pieces that"
                                 " make up the path, but you know the number of pieces is no match for the billions of"
                                 " stars in the sky.", 'jason_rd_2down', None, 'jason_jerry_crossroad')
# JERRY! -------------
jason_jerry_crossroad = Room("Jason 4-Down Jerry Crossroad", "The cobblestone path shines, lit up by the sunlight.",
                             "You walk on a cobblestone path. Beside it is grass and barley.",
                             "You walk on a decent cobblestone path. It seems to be composed of many pieces.",
                             "You hear your steps on the cobblestone. You barely see the all the pieces that make up "
                             "the path, but you think that for every star in the sky is a fragment in the ground.",
                             'jason_rd_3down', 'jerry_rd_1far', 'jason_rd_5down')
jerry_rd_1far = Room("Jerry Road 1-Right", "The cobblestone is lit up by the sunlight.",
                     "You walk on a cobblestone path. Next to the path on both sides is barley grass.",
                     "You walk on a sturdy cobblestone path. It seems to be composed of too many cobblestone pieces.",
                     "You hear your steps on the cobblestone. You barely see the blur or pieces that make up the path, "
                     "and you're not sure the number of stars is a match for the billions of pieces in the floor.",
                     None, 'tara_gates', None, 'jason_jerry_crossroad')
tara_gates = Room("Northern Gates of Tara, Jerry Road 2-Right", "The morning shows the old gates to Tara, one of the "
                                                                "minor towns.",
                  "On the north side of the path is barley. On the other, there's the town of Tara.",
                  "As the evening sun lowers on the cobblestone path, Tara's citizens are getting ready for bed.",
                  "The majority of Tara's citizens are likely asleep by now.", None, 'jerry_rd_3far')  # DOORSTEP
jerry_rd_3far = Room("Jerry Road 3-east", "The cobblestone is lit up by the sunlight.",
                     "You walk on a cobblestone path. Next to the path on both sides is barley grass.",
                     "You walk on a sturdy cobblestone path. It seems to be composed of too many cobblestone pieces.",
                     "You hear your steps on the cobblestone. You barely see the blur or pieces that make up the path, "
                     "and you're not sure the number of stars is a match for the billions of pieces in the floor.",
                     None, None, None, 'tara_gates')
# JASONS B -------------
jason_rd_5down = Room("Jason Road 5-Down", "The cobblestone path shines as if it were polished by the sunlight.",
                      "You walk on a sturdy cobblestone path. Next to the path on both sides is nice grass.",
                      "You walk on a sturdy cobblestone path. It seems to be composed of quite a bit of cobblestone "
                      "pieces.", "You hear your steps on the cobblestone path. You can barely see all the pieces that"
                                 " make up the path, but you know the number of pieces is no match for the billions of"
                                 " stars in the sky.", 'jason_jerry_crossroad', None, 'jason_rd_6down')
jason_rd_6down = Room("Jason Road 6-Down next to your patio",
                      "The cobblestone path shines as if it were polished by the sunlight.",
                      "You walk on a sturdy cobblestone path. Next to the path on both sides is nice grass.",
                      "You walk on a sturdy cobblestone path. It seems to be composed of quite a bit of cobblestone "
                      "pieces.", "You hear your steps on the cobblestone path. You can barely see all the pieces that"
                                 " make up the path, but you know the number of pieces is no match for the billions of"
                                 " stars in the sky.",
                      'jason_rd_5down', None, 'jason_rd_7down', 'patio')
jason_rd_7down = Room("Jason Road 7-Down", "The cobblestone path shines as if it were polished by the sunlight.",
                      "You walk on a sturdy cobblestone path. Next to the path on both sides is nice grass.",
                      "You walk on a sturdy cobblestone path. It seems to be composed of quite a bit of cobblestone "
                      "pieces.", "You hear your steps on the cobblestone path. You can barely see all the pieces that"
                                 " make up the path, but you know the number of pieces is no match for the billions of"
                                 " stars in the sky.", 'jason_rd_6down', None, None, 'behind_home')
jason_rd_8down = Room("Jason Road 8-Down", "The cobblestone path shines as if it were polished by the sunlight.",
                      "You walk on a sturdy cobblestone path. Next to the path on both sides is grass.",
                      "You walk on a sturdy cobblestone path. It seems to be composed of quite a bit of cobblestone "
                      "pieces.", "You hear your steps on the cobblestone path. You can barely see all the pieces that"
                                 " make up the path, but you know the number of pieces is no match for the millions of"
                                 " stars in the sky.", 'jason_rd_7down', None, 'jason_rd_9down')
jason_rd_9down = Room("Jason Road 9-Down", "The cobblestone path shines as if it were polished by the sunlight.",
                      "You walk on a sturdy cobblestone path.",
                      "You walk on a sturdy cobblestone path. It seems to be composed of quite a bit of cobblestone "
                      "pieces.", "You hear your steps on the cobblestone path. You can barely see all the pieces that"
                                 " make up the path, but you know the number of pieces is no match for the millions of"
                                 " stars in the sky.", 'jason_rd_8down', None, 'jason_rd_10down')
jason_rd_10down = Room("Jason Road 10-Down", "The cobblestone path shines as if it were polished by the sunlight.",
                       "You walk on a humble cobblestone path.",
                       "You walk on a sturdy cobblestone path. It seems to be composed of quite a bit of cobblestone "
                       "pieces.", "You hear your steps on the cobblestone path. You can barely see all the pieces that "
                                  "make up the path, but you know the number of pieces is no match for the many of "
                                  "stars in the sky.", 'jason_rd_9down', 'perry_pathway_1far', 'jason_rd_10down')

perry_pathway_1far = Room("Deviating Pathway",
                          "The morning light reveals a dirt trail leading east, deviating from Jason Road.",
                          "You walk on a dirt trail leading east, deviating from Jason Road.",
                          "You walk on a coarse dirt trail leading east from Jason Road",
                          "You walk on a coarse dirt trail revealed by the twinkling stars gazing down. "
                          "You feel a cold breeze", None, 'perry_pathway_2far', None, 'jason_rd_10down')
perry_pathway_2far = Room("Deviating Pathway...", "The morning light reveals a dirt trail leading eastward.",
                          "You walk on a dirt trail leading eastward. There's a few flowers planted next to the path.",
                          "You walk on a coarse dirt trail leading east from Jason Road. There are a few flowers "
                          "planted alongside the path.",
                          "You walk on a coarse dirt trail revealed by thousands of the twinkling stars gazing down. "
                          "You feel a cold breeze", None, 'lonely_field', None, 'perry_pathway_1far')
lonely_field = Room("Lonely Field", "The dirt trail lit by morning sunshine ends in an ocean of the humble grass "
                                    "shining in the morning sunshine.",
                    "The deviating trail ends in a lonely ocean of humble grass",
                    "The trail ends in a lonely ocean of grass as the sun sets.",
                    "Thousands of stars gaze down at the trail's end.", None, None, 'perry_pathway_2far')  # DOORSTEP
# FATE TOWER THE THIRD
fate_tower_3_garage = Room("Hiding Tower Window", "The shining sunlight fills into the room high up on the tower.",
                           "The room around you, lit up from the south window, has walls showered in brown and gold "
                           "tones. This is your ancestor's home. There is a door on the north wall of this room.",
                           "The room is filled with dim light from the window. There is a door on the north wall",
                           "The warm brown and gold tones are now hidden in the darkness from the window. This is the"
                           " old hiding place. Stars gaze at your every move from the window.")
fate_tower_darkroom = Room("ABANDONED HIDING TOWER FLOOR 5:DARKROOM",
                           "This room is a bit dark. Only a little of morning light comes in through the window. "
                           "Westward is a staircase.",
                           "This room is a bit dark. Westward is a staircase. The walls are beautifully painted with "
                           "imagery.",
                           "This room is a bit dark. Westward is a staircase.",
                           "This room is a bit dark. Westward is a staircase. Nighttime brings with it apathy.", None,
                           None, 'fate_tower_3_garage', 'fate3_fourfive_staircase')
fate3_fourfive_staircase = Room("ABANDONED HIDING TOWER FLOORS 4 AND 5 STAIRCASE",
                                "Ornate stairs connect Floors 4 and 5. (UP = FLOOR 5 DARKROOM, DOWN = FLOOR 4 HALLWAY)",
                                "Ornate stairs connect Floors 4 and 5. (UP = FLOOR 5 DARKROOM, DOWN = FLOOR 4 HALLWAY)",
                                "Ornate stairs connect Floors 4 and 5. (UP = FLOOR 5 DARKROOM, DOWN = FLOOR 4 HALLWAY)",
                                "Ornate stairs connect Floors 4 and 5. (UP = FLOOR 5 DARKROOM, DOWN = FLOOR 4 HALLWAY)",
                                )
fate3_fourfive_staircase.up = 'fate_tower_darkroom'
fate3_fourfive_staircase.down = 'fate3_floor4_hallway_south'
fate3_floor4_hallway_south = Room("ABANDONED HIDING TOWER FLOOR 5: HALLWAY, SOUTHERN SIDE",
                                  "A hallway with walls and carpets of brown and gold tones connect a westside "
                                  "staircase up and two doors on the eastside. The bedroom door is right next to you.",
                                  "A hallway with walls and carpets of brown and gold tones connect a westside "
                                  "staircase up and two doors eastside, the bedroom door being right next to you.",
                                  "To your west is a staircase up. To your east is a bedroom door.",
                                  "A hallway with walls and carpets flooded with blue tones connect westside "
                                  "staircases and two doors on the eastside, the bedroom door being right next to you.",
                                  'fate3_floor4_hallway_north', None, None, 'fate3_fourfive_staircase')
# NOTE: MAKE SURE IT PRINTS THAT THE BEDROOM DOOR IS LOCKED.
fate3_floor4_hallway_north = Room("ABANDONED HIDING TOWER FLOOR 5: HALLWAY, NORTHERN SIDE",
                                  "A hallway with walls and carpets of brown and gold tones connect a westside "
                                  "staircase down and two doors eastside. The bathroom door is right next to you.",
                                  "A hallway with walls and carpets of brown and gold tones connect a westside "
                                  "staircase down and two doors eastside, the bathroom door being right next to you.",
                                  "To your east is a bathroom door. To your west is a staircase down.",
                                  "A hallway with walls and carpets flooded with blue tones connect a westside "
                                  "staircase and two doors on the eastside, the bathroom door being right next to you.",
                                  None, 'fate3_floor4_bathroom', 'fate3_floor4_hallway_south',
                                  'fate3_threefour_staircase')
fate3_threefour_staircase = Room("ABANDONED HIDING TOWER FLOORS 3 AND 4 STAIRCASE",
                                 "Ornate stairs connect Floors 3 and 4. (UP = FLOOR 4 HALLWAY, DOWN = FLOOR 3 LIBRARY)",
                                 "Ornate stairs connect Floors 3 and 4. (UP = FLOOR 4 HALLWAY, DOWN = FLOOR 3 LIBRARY)",
                                 "Ornate stairs connect Floors 3 and 4. (UP = FLOOR 4 HALLWAY, DOWN = FLOOR 3 LIBRARY)",
                                 "Ornate stairs connect Floors 3 and 4. (UP = FLOOR 4 HALLWAY, DOWN = FLOOR 3 LIBRARY)",
                                )
fate3_threefour_staircase.up = 'fate3_floor4_hallway_north'
fate3_threefour_staircase.down = 'fate3_floor3_library'
fate3_floor3_library = Room("ABANDONED HIDING TOWER FLOOR 3:GRAND LIBRARY",
                            "You stand in a room with bookshelves lining each wall and more. In the center of a room is"
                            " a table. The up staircase to floor 4 is west.",
                            "You stand in a room with bookshelves lining each wall and more. In the center of a room is"
                            " a table. An up staircase is west.",
                            "You stand in a room with bookshelves lining each wall and more. In the center of a room is"
                            " a table.", "The up staircase back to floor 4 is west."
                            )
fate3_floor2 = Room("ABANDONED HIDING TOWER, FLOOR 2...",
                    "There are two caskets sitting next to each other with names written on each. How did you get here?"
                    " Go back upstairs.",
                    "There are two caskets sitting next to each other of a couple. I kindly suggest you go back "
                    "upstairs.",
                    "There are two caskets sitting next to each other of heroes from a legend. Go back upstairs.",
                    "These are your great great grandparents. Please go back upstairs. You have a job to do.")
fate3_floor2.up = 'fate3_floor3_library'

# ________________________________________________Characters_INSTANTIATED______________________________________

# ________________________________________________Items______INSTANTIATED________________________________________


# --------------------------Command FUNCTIONS---------------------------------
# SET TARGET
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


def unequip(string):
    if player.weapon is not None:
        if player.weapon.name.lower() in string.lower():
            player.inventory.append(player.weapon)
            player.weapon = None
            print("You unequipped your weapon.")
            return
    if player.helmet is not None:
        if player.helmet.name.lower() in string.lower():
            player.inventory.append(player.helmet)
            player.helmet = None
            print("You unequipped your headgear.")
            return
    if player.torso is not None:
        if player.torso.name.lower() in string.lower():
            player.inventory.append(player.torso)
            player.torso = None
            print("You unequipped your armor.")
            return
    if player.shoes is not None:
        if player.shoes.name.lower() in string.lower():
            player.inventory.append(player.shoes)
            player.shoes = None
            print("You unequipped your shoes.")
            return
    else:
        print("You do not seem to have this item equipped.")


def equip(target):
    if isinstance(target, Weapon) or isinstance(target, Tool):
        if player.weapon is not None:
            unequip(player.weapon.name)
        player.weapon = target
        print("You now have", target.name, "equipped as your weapon.")
        if target in player.current_location.stuff:
            player.current_location.stuff.remove(target)
        else:
            player.inventory.remove(target)
    elif isinstance(target, Headgear):
        if player.helmet is not None:
            unequip(player.helmet.name)
        player.helmet = target
        print("You now have", target.name, "equipped as your helmet.")
        if target in player.current_location.stuff:
            player.current_location.stuff.remove(target)
        else:
            player.inventory.remove(target)
    elif isinstance(target, Torso):
        if player.torso is not None:
            unequip(player.torso.name)
        player.torso = target
        print("You now have", target.name, "equipped as your armor.")
        if target in player.current_location.stuff:
            player.current_location.stuff.remove(target)
        else:
            player.inventory.remove(target)
    elif isinstance(target, Footwear):
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


# ----------------------------------------------Necessary DATA----------------------------------------
directions = ['north', 'east', 'south', 'west', 'up', 'down', 'away', 'left', 'right', 'back', 'forward']
short_directions = ['n', 'e', 's', 'w', 'u', 'd', 'ay', 'l', 'r', 'b', 'f']
ampm = "AM"
hour = 9
minutes = 0
timepass = 0
player.current_location = patio
player_name = input("Choose a name, and type it in.")
player.name = player_name
print("Your name is", player.name)

# DEMO:

demo_room = Room("DEMO ROOM!", "Room for testing, morning.", "Room for testing, noon.", "Room for testing, evening.",
                 "Room for testing, nighttime.", 'demo_room', 'demo_room', 'demo_room', 'demo_room')
player.current_location = jason_rd_5down
demo_room.stuff = [Gboots(4, "LEATHER"), Gelmet(5, "LEATHER"), Generic("Bag", "Just a bag.", "LIGHT", []),
                   Standard("Sword", "a sword...", "MELEE"), Standard("Bow", "Just a bow", "RANGED"), Gorso(6, "IRON"),
                   Money(43)]
jason_rd_5down.characters = [Character("Jenn", jason_rd_5down, 400, 5, Traveler(True), Ord("FLAME"), Kinghelm("Jenn")),
                        Character("Jeff", jason_rd_5down, 4000, 5, Traveler(False), Standard("Regular Sword",
                                                                                            "pretty cool", "MELEE")),
                             Character("Orc1", jason_rd_5down, 500, 5, Hostile(), None, Gelmet(4, "IRON"))]

# ___________________________________________________CONTROLLER__________________________________________________
playing = True
while playing:
    # __________________"SCREEN":
    print()
    print(player.current_location.name + ",", "%d hours %d minutes in %s" % (hour, minutes, ampm))
    # Printing Time
    if ampm == "AM":
        if hour == 12:
            print(player.current_location.night_description)
        elif hour >= 5:
            print(player.current_location.morning_description)
        else:
            print(player.current_location.night_description)
    else:
        if hour == 12:
            print(player.current_location.noon_description)
        elif hour <= 5:
            print(player.current_location.noon_description)
        elif hour <= 8:
            print(player.current_location.evening_description)
        else:
            print(player.current_location.night_description)
    if 2 > len(player.current_location.characters) > 0:
        print()
        print(">>> %s is here." % player.current_location.characters[0].name)
    elif len(player.current_location.characters) >= 2:
        characters = []
        for i in range(len(player.current_location.characters)):
            characters.append(player.current_location.characters[i].name)
        print(">>>", ", ".join(characters), "are here.")
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
    command = input(">_")  # ----------------ENTER COMMAND:
    if command.lower() in ['q', 'quit', 'exit', 'goodbye']:  # -----------QUIT GAME
        playing = False
        print("%s left the game" % player_name)
    elif command.lower() in ['stats', 'player statistics']:
        print()
        print("PLAYER STATISTICS.")
        print("NAME:", player.name)
        print("PLAYER HEALTH: %s, ATTACK_POWER: %d, MONEY: %s" %
              (player.health, player.attack_power, player.money))
        equips = []
        isequipped = [player.weapon, player.helmet, player.torso, player.shoes]
        for i in range(len(isequipped)):
            if isequipped[i] is not None:
                equips.append(isequipped[i].name)
        if len(equips) == 0:
            print("EQUIPPED: You have nothing equipped.")
        else:
            print("EQUIPPED:", ", ".join(equips))

        if len(player.inventory) > 1:
            inventory = []
            for i in range(len(player.inventory)):
                inventory.append(player.inventory[i].name)
            inventory = ", ".join(inventory)
            print("INVENTORY:", inventory)
        elif len(player.inventory) > 0:
            print("INVENTORY:", player.inventory[0])
        else:
            print("INVENTORY: NOTHING")

    elif command.lower() in directions:  # -----------------MOVE ROOM A
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
            timepass += 1
        except KeyError:
            print("You can't go that way")
    elif "examine" in command.lower() or "look at" in command.lower() or "observe" in command.lower():  # EXAMINE
        item_target = set_item_target(command.lower(), player.inventory)
        if item_target is None:
            item_target = set_item_target(command.lower(), player.current_location.stuff)
        if item_target is not None:
            print(item_target.name, "...")
            print(item_target.description)
        else:
            print("There doesn't seem to be anything in your inventory or this room by that name.")
    elif "unequip" in command.lower() or "take off" in command.lower(): # --------------UNEQUIP ITEM
        unequip(command.lower())
    elif "equip" in command.lower() or "put on" in command.lower() or "wear" in command.lower():  # -------EQUIP ITEM
        item_target = set_item_target(command.lower(), player.inventory)
        if item_target is None:
            item_target = set_item_target(command.lower(), player.current_location.stuff)
        if item_target is not None:
            equip(item_target)
        else:
            print("There doesn't seem to be anything here by that name you can equip.")
    elif "pick up" in command.lower() or "take" in command.lower() or "get" in command.lower():  # -----TAKE ITEM
        item_target = set_item_target(command.lower(), player.current_location.stuff)
        if item_target is not None:
            player.inventory.append(item_target)
            player.current_location.stuff.remove(item_target)
            print("You took the", item_target.name)
        elif "money" in command.lower():
            for i in range(len(player.current_location.stuff)):
                if isinstance((player.current_location.stuff[i]), Money):
                    player.money += player.current_location.stuff[i].amount
                    player.current_location.stuff.remove(player.current_location.stuff[i])
        else:
            print("There's nothing here of that name you can pick up.")
    elif "drop" in command.lower() or "leave" in command.lower():  # ----------------------DROP ITEM
        item_target = set_item_target(command.lower(), player.inventory)
        if item_target is not None:
            player.current_location.stuff.append(item_target)
            player.inventory.remove(item_target)
            print("You dropped", item_target.name)
        else:
            print("There's nothing in your inventory or that name.")
    elif "wait" in command.lower():  # --------------------------------------WAIT
        print("You want to wait?")
        wait = 0
        which = input("In hours or minutes?")
        if "hour" in which:
            wait = input("How many hours? (Must be 12 or below.")
            if int(wait) > 12:
                print("No!")
                wait = input("How many hours? (Must be 12 or below.)")
            hour += int(wait)
            if hour > 12:
                hour -= 12
                if ampm == "AM":
                    ampm = "PM"
                else:
                    ampm = "AM"
        else:
            wait = input("How many minutes? (Must be 60 or below.)")
            if int(wait) > 60:
                print("No!")
                wait = input("How many minutes? (Must be 60 or below.)")
            minutes += int(wait)
            if minutes >= 60:
                minutes -= 60
                hour += 1
            if hour > 12:
                hour -= 12
                if ampm == "AM":
                    ampm = "PM"
                else:
                    ampm = "AM"
    elif command.lower() in short_directions:  # ---------------MOVE ROOM B
        pos = short_directions.index(command.lower())
        command = directions[pos]
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
            timepass += 1
        except KeyError:
            print("You can't go that way")
    elif "inventory" in command.lower() or command.lower() in "i":  # -------------------CHECK INVENTORY
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
    elif "attack" in command.lower() or "hit" in command.lower(): # ----------ATTACK!
        target = set_character_target(command.lower(), player.current_location.characters)
        if target is not None:
            player.attack(target)
        else:
            print("Attack who?")
    else:
        print("Command Not Found...")
        timepass += 1
    # _____________RESULT BESIDES COMMAND RESULT: (Idea: "action" and "result" variables can trigger entity behaviours.)
    characters_in_play = []
    for i in range(len(player.current_location.characters)):
        characters_in_play.append(player.current_location.characters[i])
    for i in range(len(characters_in_play)):
        print(characters_in_play[i].ai.conditions)
        print(characters_in_play[i].ai.action)
        characters_in_play[i].react(player, command.upper())
        characters_in_play[i].behave()
        print(characters_in_play[i].ai.conditions)
        print(characters_in_play[i].ai.action)
    characters_in_play = []

    if timepass == 0:  # TIME PASSES
        pass
    else:
        minutes += timepass
        if minutes >= 60:
            minutes -= 60
            hour += 1
            if hour > 12:
                hour = 1
            if hour == 12:
                if ampm == "AM":
                    ampm = "PM"
                else:
                    ampm = "AM"
        timepass = 0
    if player.health <= 0:
        player.dead = True
        print("It seems that you have died.")
        playing = False
    print()
    print("---" * 9)
