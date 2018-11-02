import random
win = False
minimum = int(input("Give me a number that will be your minimum:"))
maximum = int(input("Now we need a maximum:"))
guesses = int(input("How many guesses would you like?"))
the_number = random.randint(minimum, maximum)


print("There is a number from %s to %s" % (minimum, maximum))
print()
print("You have %s guesses as to what this number is." % guesses)

while guesses > 0:
    guess = int(input("What is the number:"))
    if guess == the_number:
        print("Hey, you got it! Good job!")
        guesses = 0
        win = True

    elif guess > the_number:
        print("...lower...")
        guesses = guesses - 1
    else:
        print("...higher...")
        guesses = guesses - 1
    print("%s guesses remain." % guesses)


def game_end():
    if win:
        print()
        print("You won!")
    else:
        print("Try again next time.")


game_end()

