import random
#  OOP - https://realpython.com/python3-object-oriented-programming/
#  Dictionary - https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary
class Snop:
    def __init__(self, name, age, cool):

        species = 'mammal'
        self.cool = True
        self.name = name
        self.age = age
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


names = ["Jason", "Jeff", "Randy", "Sunny", "Fluffy", "Mo", "Larry", "Mary", "Bo", "Lovely", "Beatrice", "Ari", "Mason",
         "Grue"]
items_values = {"Bouncy Ball":2, "Bracelet": 7, "Pencil":1, "Gifts":4, "Pet Fluff":10}
items = ["Bouncy Ball", "Bracelet", "Pencil", "Gifts", "Pet Fluff"]
like = []
not_like = []
possessions = []
thing = "Nothing"
for i in range(random.randint(1, len(items))):
    thing = random.choice(items)
    if thing not in like:
        like.append(thing)
for i in range(random.randint(1, len(items))):
    thing = random.choice(items)
    if thing not in not_like and thing not in like:
        not_like.append(thing)
for i in range(random.randint(1, len(items))):
    trufalse = [True, False]
    have = random.choice(trufalse)
    thing = random.choice(items)
    if have:
        possessions.append(thing)
multiplier = random.randint(1, 5)
value = random.randint(1, 10)
richness = value * multiplier
nice = random.randint(1, 10)
new_snop = Snop(random.choice(names), random.randint(20, 30), random.choice(trufalse), like, not_like, possessions,
                richness, nice)
list.append(snop_population, new_snop)


print()
print("New scenario:")
print("There are %s Snops." % len(snop_population))
