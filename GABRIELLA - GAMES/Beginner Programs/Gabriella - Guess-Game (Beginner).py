import random
win = False
minimum = 1
maximum = 10
guesses = 5
the_number = random.randint(1, 10)


print("I'm thinking of a number from %s to %s" % (minimum, maximum))
print()
print("You have 5 guesses as to what this number is.")

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
        print("...Try a higher number.")
        guesses = guesses - 1
    print("You have %s guesses left." % guesses)


def game_end():
    if win:
        print()
        print("You won!")
    else:
        print("Try again next time.")


game_end()


"""
again = input("Try again?")


if again == "Yes" or "yes" or "sure" or "Try again":
    guesses = 5
    the_number = random.randint(1, 10)
else:
        print("Alright...")
"""
