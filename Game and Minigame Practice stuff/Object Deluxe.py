import random


class Pet(object):  # Helper Pet
    def __init__(self, name, items):
        self.name = name  # This is his name
        self.skill = 2  # This is his efficiency in all of his tasks.
        self.money = 5  # This is what he needs to go buy you your groceries.
        self.max_health = 50  # This is his maximum health cap.
        self.health = 40  # When this reaches zero, your pet passes out.
        self.items = items  # This is what he is carrying in his pockets.

    def speak(self):  # Communicate with your pet
        print()
        print("You ask him to speak.")
        self.health += random.randint(0, 1)
        if self.skill < 3 or self.health <= 0:
            print("He does not respond.")
        elif self.skill < 10:
            print("He cannot speak. He does not use speech.")
        else:
            print("He can't speak, but instead he is using gestures.")
        self.skill += random.randint(0, 1)
        return

    def do_trick(self):
        print()
        print("You ask him to do a trick")
        if self.skill <= 3:
            print("He does not have enough skill.")
            print("He tries to do a cartwheel, but he tumbles over.")
            print("Have him do another trick to practice more.")
            chance = random.randint(1, 4)
            if chance == 1:
                return
            if chance == 2 or 4:
                self.skill += random.randint(1, 3)
            if chance == 3 or 4:
                self.health -= random.randint(1, 3)
        elif 3 < self.skill <= 15:
            print("He does a successful cartwheel. You are both pleased with his skills.")
            chance = random.randint(1, 10)
            if chance == 1:
                return
            if 1 < chance < 5:
                self.skill += random.randint(1, 3)
                print("He is getting better.")
            if chance > 7:
                self.health -= random.randint(1, 3)
                print("He may have tripped at the end of that cartwheel, though.")
        self.skill += random.randint(0, 1)
        return

    def give_money(self):
        print("Jeff has %d coins." % self.money)
        print("You want to give %s some coins." % self.name)
        give = ""
        while not give.isdigit():
            give = input("How much money do you want to give him? (Enter a number):")
        self.money += int(give)
        print("%s now has %d coins." % (self.name, self.money))
        return ""

    def stats(self):  # Status
        print()
        self.health += random.randint(0, 1)
        print("You ask him about his status.")
        if self.health <= 0:
            print("He is asleep. He may wake up soon, but you must wait...")
        elif 2 < self.skill < 3:
            print("He does not respond.")
            print("Somehow you can tell that his skill level is at %d" % self.skill)
            print("He needs more skill level to communicate.")
        elif self.skill <= 5:
            print("He cannot speak, but somehow he communicates to you that...")
            print("His skill level is %d" % self.skill)
            print("His maximum health is %d, and his health is at %d." % (self.max_health, self.health))
            print("He has %d coins." % self.money)
            if len(self.items) > 0:
                print("He is carrying %s" % self.items)
            else:
                print("He is not carrying anything.")
        elif 5 < self.skill < 15:
            print("He can't speak, but instead he is using gestures to tell you that...")
            print("His skill level is %d" % self.skill)
            print("His maximum health is %d, and his health is at %d." % (self.max_health, self.health))
            print("He has %d coins." % self.money)
            if len(self.items) > 0:
                print("He is carrying %s" % self.items)
            else:
                print("He is not carrying anything.")
        elif self.skill >= 15:
            print("He can't speak, but instead he is using gestures to tell you that...")
            print("His name is %s" % self.name)
            print("His skill level is %d" % self.skill)
            print("His maximum health is %d, and his health is at %d." % (self.max_health, self.health))
            print("He has %d coins." % self.money)
            if len(self.items) > 0:
                print("He is carrying %s" % self.items)
            else:
                print("He is not carrying anything.")
        self.skill += random.randint(0, 1)
        return


Day = True
pet_name = input("You just received your new helper pet! Give him a name:")
pet_pocket = []
pet = Pet(pet_name, pet_pocket)

print(pet.speak())
print(pet.do_trick())
print(pet.stats())

speak_commands = ["speak", "talk", "say something"]
trick_commands = ["do trick", "do something"]

while Day:
    print()
    print("Your pet is ready to help you.")
    command = input("What do you want him to do?")
    if command in speak_commands:
        print(pet.speak())
    elif command in trick_commands:
        print()

