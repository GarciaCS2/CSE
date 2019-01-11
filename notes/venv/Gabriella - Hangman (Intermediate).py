import random
word_bank = ["Super", "Word", "Bow", "Read", "Maverick", "Awesome", "Trapdoor", "Pizzicato", "Embezzled", "Garnish",
             "Math", "Python", "Variable", "Concatenation", "Fjord", "Crypt", "Bagpipes", "Haiku", "Jazzy", "Banjo",
             "River", "Discombobulated", "Zippy", "Gazebo", "Intermediate", "Croquet", "Aerobics", "Anaerobic"]

word = random.choice(word_bank)
letters_guessed = []
guesses = 8
blank = ["_" * len(word)]
case = "lower"
win = False
display = "".join(blank)
def dev_details():
    print("WORD = " + word + ", %s LETTERS" % len(word))
    print(blank)
    print(display)
    print("GUESSES = " + str(guesses))


dev_details()

while win == False and guesses > 0:
    print()
    print(letters_guessed)

    guess_letter = input("Give me a letter:")
    if guess_letter.lower in letters_guessed:
        print("You have already guessed this letter.")
    elif guess_letter.lower() in word.lower():
        print("Yes, %s is in the word." % guess_letter)
        letters_guessed.append(guess_letter.lower())
        blank[(word.lower()).index(guess_letter.lower())] = word[(word.lower()).index(guess_letter.lower())]
    elif guess_letter not in word.lower() or guess_letter not in word.upper():
        print("No, %s is not in the word. Sorry!" % guess_letter)
        letters_guessed.append(guess_letter.lower())
        guesses -= 1
    print(display)


