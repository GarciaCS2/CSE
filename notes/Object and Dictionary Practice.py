import random
#  OOP - https://realpython.com/python3-object-oriented-programming/
#  Dictionary - https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary
class Snop:
    def __init__(self, name, age, cool, fact, complement):

        species = 'mammal'
        self.cool = True
        self.name = name
        self.age = age
        self.fact = fact
        self.complement = complement

    def describe(self):
        return "{} is {}. He {}.".format(self.name, self.age, self.fact)

    def give_kudos(self):
        return "{} says, '{}'".format(self.name, self.complement)
    pass


jeff = Snop('Jeff', 14, True, "likes memes", "You're cool.")
avery = Snop('Avery', 10, True, "can do gymnastics", "Good work.")

snop_population = [jeff, avery]

print(jeff == avery)
print("{0} is a Snop. He is {1}.".format(jeff.name, jeff.age))


def find_cool_snop():
    cool_snops = 0
    for i in range(len(snop_population)):
        if snop_population[i].cool:
            cool_snops += 1
    print("There are %s cool Snops." % cool_snops)
    if cool_snops == len(snop_population):
        print("All the Snops are cool!")


find_cool_snop()



command = input("")
if "hi" in command.lower():
    if "jeff" in command.lower():
print(jeff.give_kudos())
