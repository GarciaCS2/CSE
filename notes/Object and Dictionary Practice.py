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

