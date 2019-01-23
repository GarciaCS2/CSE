import random
#  OOP - https://realpython.com/python3-object-oriented-programming/
#  Dictionary - https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary
class Snop:
    def __init__(self, name, age, cool, likes, dislikes, stuff, tokens, niceness):

        species = 'mammal'
        self.cool = True
        self.name = name
        self.age = age
        self.likes = likes
        self.dislikes = dislikes
        self.stuff = stuff
        self.money = tokens
        self.niceness = niceness
    pass

jeff = Snop('Jeff', 14, True)
avery = Snop('Avery', 10, True)

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


def gen_snops():
    names = ["Jason", "Jeff", "Randy", "Sunny", "Fluffy", "Mo", "Larry", "Mary", "Bo"]
    items = {"Bouncy Ball":2, "Bracelet": 7, "Pencil":1, "Gifts":4, "Pet Fluff":10}
    for i in range(random.int(1, 15)):
        like =
    list.append(snop_population, Snop(random.choice(names), random.int(20, 30), random.choice(True, False),
                                      like, not_like, stuff, tokens, niceness)

