"""
print("Hello World!")

# This is a comment. This has no effect on the code
# but this does allow me to do things. I can:
# 1. Make notes to myself
# 2. Comment pieces of code that do not work
# 3. Make my code easier to read


print("Look at what happens here. Is there any space?")
print()
print()
print("There should be a couple blank lines here.")
# Math
print(3 + 5)
print(5 - 2)
print(3 * 4)
print(6 / 2)

print("Figure this out...")
print(6 // 2)
print(5 // 2)
print(9 // 6)

print("Here is another one...")
print(6 % 2)
print(5 % 2)
print(11 % 4)  # Modulus (Remainder)

# Powers
# What is 2^20?
print(2 ** 20)

# Taking input
# %s. is the symbol for "String"
name = input("What is your name?")
print("Hello, %s." % name)

age = input("How old are you? >_")
print("%s?!? You belong in a museum." % age)
print()
print("%s is really old. They are %s years old." % (name, age))

# Variable Assignments
car_name = "Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 16
car_miles_per_gallon = 0.01

# Make it print "I have a car called Wiebe Mobile. It is a Tesla."

print("I have a car called %s. It is a %s." % (car_name, car_type))

# Recasting
real_age = int(input("How old are you again?"))
hidden_age = real_age + 5
print("This is your real age: %d" % hidden_age)
"""


"""
This is a multi-line comment
Anything between the "s is not run.
"""


# Functions
def say_it():
    print("Hello World!")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


print()

# Distance Formula
# dist = sq((x1 - x2)^2 + (y1 - y2)^2)


def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 5, 12)

# Loops
for i in range(5):  # This gives the numbers 0 through 4
    say_it()


print()


for i in range(10):
    print(i+1)


print()


for i in range(5):
    f(i)


# While loops
a = 0
while a < 10:
    print(a)
    a += 1  # This is the same as saying a = a + 1


"""
At the moment you START the loop:
For loops - Use when you know EXACTLY how many iterations
While loops - Use when you DON'T know how many iterations
"""

# Control Structures (If statements)
sunny = True
if sunny:
    print("Go outside")


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(82)
print(your_grade)


# "Random" Notes
import random  # This should be on line 1
print(random.randint(0,100))
print()

# Equality Statements
print(5 > 3)  # Greater Than
print(5 >= 3)  # Equal to;Is set to
print(3 == 3)  # Is it equal?
print(3 != 4)  #
"""
a = 3  # A is set to 3
a == 3  # Is a equal to 3?
"""

# Creating a list
colors = ["aquamarine blue", "forest green", "sunshine yellow", "marigold", "turquoise", "lemon",
          "coffee brown", "mayo", "indigo purple"]  # USE SQUARE BRACKETS!!!!!
print(colors[0])  # index
print(colors[1])

# Length of the list
print("There are %d colors in this list" % len(colors))

# Changing Elements in a list
colors[1] = "Green"
print(colors)

# Looping through lists
for blahblahblah in colors:
    print(blahblahblah)

"""
1. Make a list with 7 items
2. change the 3rd thing in the list
3. print the item
4. print the full list
"""

items = ["cool item", "decent item", "bad item", "amazing item", "mediocre item", "best item", "insignificant item"]
items[2] = "not so bad item"
print(items[3])
print(items)
print("The last thing in the list is this %s" % items[len(items)-1])

# Slicing a list
print(items[1:3])
print(items[1:4])
print(items[1:])
print(items[:4])


food_list = ["burrito", "eggs", "taco", "pizza", "oranges", "rice", "toast", "pie", "spaghetti", "tuna",
             "chicken", "calamari", "oatmeal", "yogurt", "cereal", "salad", "noodles", "broccoli", "beef",
             "apple", "steak"]
print(len(food_list))

# Adding stuff to a list
food_list.append("bacon")
food_list.append("more eggs")
# Notice that everything is object.method(parameters)
print(food_list)
food_list.insert(1, "eggo waffles")
print(food_list)

# Removing things from a list
food_list.remove("salad")

# Assignment
three_items = ["cat", "dog", "bird"]
print(three_items)
list.append(three_items, "hamster")
print(three_items)
three_items.remove("bird")
print(three_items)


# Tuples
brands = ("apple", "samsung", "HTC")   # Notice the parentheses
# Like a list, except it is "immutable"
# immutable...im-mutable. mutate, to change.
# "Cannot be changed." You can't modify Tuples! They're immutable!
# (Tuple), [List], {Dictionary}

# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)

# Find the index of an item
print(food_list.index("chicken"))


# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

# Turn a list into a string
print("".join(list1))
print()

for i in range(len(list1)):  # i goes through all indicies
    if list1[i] == "u":  # if we find a U
        list1.pop(i)  # remove the i-th index
        list1.insert(i, "*")  # Put a * there instead
print(list1)

# range is actually 0 thru 8 to count through 9. It goes through every single index of list1.
# accesses each of the locations, asking if it is "u". Is this "u"? Then it inserts a star instead.
# or

for character in list1:
    if character == "u":
        # replace with a *
        current_index = list1.index(character)
        list1.pop(current_index)
        list1.insert(current_index, "*")

# Same thing, except it goes through characters rather than indeces.
