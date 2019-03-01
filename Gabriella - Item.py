class Item(object):
    def __init__(self, name, description, location=None):
        self.name = name
        self.description = description
        self.location = location


class Equipment(Item):
    def __init__(self, name, description, condition='New', function):
        super(Equipment, self).__init__(name, description)
        self.condition = condition
        self.function = function
