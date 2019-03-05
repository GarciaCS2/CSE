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


class Weapon(Equipment):
    def __init__(self, name, description, location, weight, attack_power, reach):
        super(Weapon, self).__init__(name, description, location, weight)
        self.attack_power = attack_power

        self.range_or_reach = reach


class Generic(Weapon):
    def __init__(self, name, description, location, weight, attack_power, reach, type):
        super(Generic, self).__init__(name, description, location, 'MODERATE', 70, reach)
        self.type = type
