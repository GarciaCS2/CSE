import string
print("Hello World!")

# This is a single line comment.

cars = 5
driving = True  # In Java, there is no caps for this.
vehicle = "car"

print("I have %d %ss." % (cars, vehicle))

print("I have " + str(cars) + " cars.")  # concatenation

age = input("How old are you?")
if age.isdigit():
    age = int(age)
else:
    print("I need a number...")
    age = input("How old are you?")
    if age.isdigit():
        age = int(age)
    else:
        print("Perhaps you're too young...")
        age = 2

print("This person is %d years old." % age)
if 0 < age < 21:
    print("They're quite young")
elif age > 75:
    print("They're quite old.")
elif age == 0:
    print("They don't exist...")

colors = ["green", "blue", "purple", "sunshine yellow", "red"]
list.append(colors, "cool turquoise")
print(colors)
# colors.remove(colors[0])
colors.pop(0)
print(colors)

print(colors[2])

print(len(colors))

print(list(string.ascii_letters))
print(string.digits)
#  May 29 - late work, May 24 - showcase day, June 6 - last day of school
print()
dictionary = {"Late Work", "Showcase Day", "Last Day of School"}
print(dictionary)
dictionary = {"Showcase Day":24, "Late Work":29, "Last Day of School":6}  # Key:Value
print(dictionary)
print(dictionary["Showcase Day"])
dictionary["Today"] = 17
print(dictionary)
