class Vehicle(object):
    def __init__(self, name, awesomeness=None):
        self.name = name
        self.awesomeness = awesomeness


class Car(Vehicle):
    def __init__(self, name, milage):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100
        self.milage = milage

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the car turns on.")
        print("Your car is at %d fuel" % self.fuel)

    def move_forward(self):
        if not self.engine_status or self.fuel <= 0:
            return
        self.fuel -= 1
        print("The car moves forward")

    def turn_left(self):
        if not self.engine_status or self.fuel <= 0:
            return
        self.fuel -= 1
        print("The car turns left")

    def turn_right(self):
        if not self.engine_status or self.fuel <= 0:
            return
        self.fuel -= 1
        print("The car turns right")

    def turn_off(self):
        self.engine_status = False
        print("You turn off the car.")


class Impala(Car):
    def __init__(self):
        super(Impala, self).__init__("Impala", 25)


class KeylessCar(Car):
    def __init__(self, name, milage):
        super(KeylessCar, self).__init__(name, milage)

    def start_enigine(self):
        self.engine_status = True
        print("You push the button and the car turns on.")


wiebe_car = KeylessCar("Tesla", 125)
wiebe_car.start_engine()

jacob_car = Impala()
jacob_car.start_engine()
jacob_car.move_forward()
jacob_car.turn_left()
jacob_car.move_forward()
jacob_car.turn_off()
