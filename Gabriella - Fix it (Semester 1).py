age = input("How old are you?")
height = input("How tall are you?", )
weight = input("How much do you weigh?")

print("So, you're %s old, %s tall and %s heavy." % (age, height, weight))


print("'Let's practice everything.")
print("'You'd need to know 'bout escapes'")
print("that do newlines and tabs.")


poem = ["The lovely world", "with logic so firmly planted",
        "cannot discern the needs of love nor comprehend passion from intuition",
        "and requires an explanation where there is none."]

print("--------------")

for i in range(len(poem)):
    print(poem[i])
print("--------------")


five = 10 - (2 + 3)
print("This should be five: %s" % five)


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars/100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: %d" % start_point)
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")
elif people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")
elif people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

elif people <= dogs:
    print("People are less than or equal to dogs.")
elif people == dogs:
    print("People are dogs.")
