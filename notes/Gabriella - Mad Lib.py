print("Welcome to this Mad Lib. Please, feed me words.")

name = input("Give me a name for a person:")
number1 = input("Give me a number:")
noun1 = input("Give me a plural noun:")
noun2 = input("Give me a singular noun:")
place1 = input("Give me a place:")
distance1 = input("Give me a number:")
dist_measurement = input("Give me a unit of distance measurement:")
number2 = input("Give me another number.")
measurement1 = input("I need a unit of measurement:")
noun3 = input("Another noun, please:")
measurement2 = input("I need another unit of measurement:")
number4 = input("I need another number:")
measurement3 = input("Another unit of measurement, please:")
print()

print()

# Story

print("MATH PERFORMANCE TASK")
print("Read the question and then solve.")
print("%s has %s %s." % (name, number1, noun1))
print("To build a %s to get to %s, which is %s %ss far away from the %s," %(noun2, place1, distance1, dist_measurement, noun3)
print("%s needs the %s to be %s %s long, %s %s wide, and %s %s tall." %(name, noun1, number2, measurement1, number2, measurement2, number4, measurement3))
