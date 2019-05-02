import random
win = False
print("Welcome to Guess Game.")
minimum = int(input("Give me a number that will be your minimum:"))
maximum = int(input("Now we need a maximum:"))
guesses = int(input("How many guesses would you like?"))
the_number = random.randint(minimum, maximum)


print("There is a number from %s to %s" % (minimum, maximum))
print()
print("You have %s tries to find it." % guesses)

while guesses > 0:
    guess = int(input("What is the number:"))
    if guess == the_number:
        print("Yes, that's it.")
        guesses = 0
        win = True

    elif guess > the_number:
        print("...lower...")
        guesses = guesses - 1
    else:
        print("...higher...")
        guesses = guesses - 1
    print("%s guesses remain." % guesses)


print("The number was %s" %the_number)
def game_end():
    if win:
        print()
        print("You won!")
    else:
        print("Try again next time.")


game_end()

