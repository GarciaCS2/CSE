print("Welcome to this Mad Lib. Please, feed me words.")

# inputs

name = input("Give me a name for a person:")
number1 = input("Give me a number:")
noun1 = input("Give me a plural noun:")
noun2 = input("Give me a singular noun:")
verb1 = input("Give me a verb not ending in 'ing':")
place1 = input("Give me a place:")
distance1 = input("Give me a number:")
noun4 = input("Noun? Plural?")
dist_measurement = input("Distance measurement:")
number2 = input("Give me another number.")
measurement1 = input("I need a unit of measurement:")
number3 = input("Another number:")
adjective1 = input("An adjective, if you will:")
noun3 = input("Another noun, either plural or singular, please:")
measurement2 = input("I need another unit of measurement:")
number4 = input("I need another number:")
measurement3 = input("Another unit of measurement, please:")
adjective2 = input("Another adjective:")

print()

print()

# Story

print("MATH PERFORMANCE TASK")
print("Read the question and then solve.")
print()
print("%s has %s %s." % (name, number1, noun1))
print("To build a %s to get to %s, which is %s %s far away from the %s %s," % (noun2, place1, distance1,
                                                                               dist_measurement, adjective2, noun3))
print("%s needs the %s to be %s %s long, %s %s wide, and %s %s tall." % (name, noun1, number2, measurement1, number3,
                                                                         measurement2, number4, measurement3))
print("Based on this, how many %s does %s need to %s to make the %s %s?" % (noun4, name, verb1, noun1, adjective1))
