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


class Gorso(Torso):
    def __init__(self, location, protection, material):
        super(Gorso, self).__init__("Generic Torso Armor", "Just your everyday armor", location, protection, material,
                                    None)


class Footwear(Armour):
    def __init__(self, name, description, location, protection, material, blessing):
        super(Footwear, self).__init__(name, description, location, 'MODERATE', protection, material, blessing)


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
    def __init__(self, location, contents, fill=0, color="purple", ):
        super(Thermos, self).__init__("Thermos", "A %s cup meant to hold liquids, hot or cold." % self.color, location,
                                      'LIGHT', 'LIQUIDS', 'LABEL', contents)
        self.fill = fill  # %0 is Empty, %100 is Filled
        self.color = color


class Bottle(Carrier):   # INSTANTIABLE Bottle (You can throw it)
    def __init__(self, location, material, contents):
        super(Bottle, self).__init__("Thermos", ("A %s bottle filled with %s" % self.material, self.contents), location,
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


class Weapon(Equipment):
    def __init__(self, name, description, location, weight, attack_power: int, reach):
        super(Weapon, self).__init__(name, description, location, weight)
        self.attack_power = attack_power
        self.range_or_reach = reach


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


regular_barrel = Mallobarrel()


class Marshooter(Weapon):  # INSTANTIABLE Marshmallow Shooter (Sow >>> Sky-Bow)
    def __init__(self, location, barrel=regular_barrel):  # Trying to link mallobarrel to marshooter
        super(Marshooter, self).__init__("Rapid-Fire Marshmallow Shooter", "It's so fast, most enemies can't handle it!"
                                         "", location, 'LIGHT', 20, 'FAR')
        self.barrel = barrel


class Character(object):
    def __init__(self, name, health, weapon=None, helmet=None, torso=None, boots=None):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.helmet = helmet
        self.torso = torso
        self.boots = boots
        self.armor = 0

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
            self.armor += self.boots.protection
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

    def attack(self, target):
        print("Attack! ", self.name, "hit ", target.name, " for ", self.weapon.attack_power, " damage.")
        target.take_damage(self.weapon.attack_power)


sword = Standard("Some sword.", "Just a generic sword thing.", "INSERT ROOM HERE", 'MELEE')
marsh = Marshooter(None, Mallobarrel(None, 100, 100))

marsh.barrel.count_mallows()

cool_torso = Gorso(None, 20, 'IRON')


knight = Character("The Knight", 100, sword, None, cool_torso)
cool_helmet = Kinghelm(None, knight)
knight.helmet = cool_helmet
good_sword = Ord(None, 'FIRE')
other_helm = Gelmet(None, 20, 'IRON')
other_torso = Gorso(None, 30, 'IRON')
orc = Character("Wievel", 1000, good_sword, other_helm, other_torso)

orc.attack(knight)
knight.attack(orc)
