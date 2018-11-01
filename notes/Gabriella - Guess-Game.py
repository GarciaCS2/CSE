import random
did_you_win = False
minimum = 1
maximum = 10
guesses = 5
THE_NUMBER = random.randint(1, 10)
print("I'm thinking of a number from %s to %s" % (minimum, maximum))
print()
print("You have 5 guesses as to what this number is.")

while guesses > 0:
    guess = int(input("What is the number:"))
    if guess == THE_NUMBER:
        print("Hey, you got it! Good job!")
        guesses = 0
        did_you_win = True

    elif guess > THE_NUMBER:
        print("...lower...")
        guesses = guesses - 1
    else:
        print("...Try a higher number.")
        guesses = guesses - 1
    print("You have %s guesses left." % guesses)

"""
if did_you_win=True:
    print()
    print("You won!")
else:
    print("Try again next time.")


def reset_game():
    guesses = 5
    THE_NUMBER = random.randint(1, 10)



again = input("Try again?")

if reset = "Yes" or "yes" or "Sure":
    reset_game()
else:
    print
"""