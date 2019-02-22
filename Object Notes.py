import Special_Random


class Phone(object):  # Constructor
    def __init__(self, carrier, charge_left=50):
        # These are attributes that a phone has.
        # These should all be relevant to our program
        self.screen = True  # "Attributes, Private instance variables, Fields"
        self.camera = 2
        self.microphone = True
        self.carrier = carrier
        self.battery_left = charge_left

    def charge(self, time):  # Functions, (Methods, Java.)
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100 # Mutation process

    def make_call(self, duration):
        if not self.screen:
            print("You can't make a phone call.")
            print("Your screen is broken.")
            return
        battery_loss_per_minute = 5
        if self.battery_left <= 0:
            print("You can't. The phone is dead.")
            return
        self.battery_left -= duration * battery_loss_per_minute
        if self.battery_left < 0:
            self.battery_left = 0
            print("Your phone dies during the conversation")
        elif self.battery_left == 0:
            print("Your phone dies at the end of the conversation.")
        else:
            print("You successfully make the phone call.")
            print("Your phone is now at %s" % self.battery_left)

    def smash_phone(self):
        print("SMASH!!!!")
        print("It broke. Whoops!")
        self.screen = False


# Initialize Objects
my_phone = Phone("T-Mobile", 100)
your_phone = Phone("Bell", 0)
default_phone = Phone("Verizon")

my_phone.make_call(60)
my_phone.make_call(10)
print()
your_phone.make_call(5)
your_phone.smash_phone()
your_phone.make_call(5)
print()
default_phone.make_call(5)

print(Special_Random.RandomWiebe.my_random())


""" # Option 1 - Define as we go
R19A = Room("Mr.Weibe's Room")
parking_lot = Room("Parking Lot", None, R19A)

R19A.north = parking_lot  # You cannot connect earlier rooms to later rooms until after the later rooms are made.
# EASIER CONTROLS, LESS LIKELY TO MAKE SPELLING MISTAKES, LONGER CODE, MORE LIKELY TO MISS A LINK 

# Option 2 - Set all at once
R19A = Room("Mr.Weibe's Room", 'parking_lot') # Uses Strings
parking_lot = Room("Parking Lot", None, "R19A")
# TAKES MORE TIME TO GO THROUGH AND CHANGE EACH NAME OR FIX MISPELLINGS """
