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

def dev_details():
    print("WORD = " + word + ", %s LETTERS" % len(word))
    print(blank)
    print("".join(blank))
    print("GUESSES = " + str(guesses))


dev_details()

while win == False and guesses > 0:
    print()
    print(letters_guessed)
    print(blank)
    guess_letter = input("Give me a letter:")
    if guess_letter in letters_guessed:
        print("You have already guessed this letter.")
    elif guess_letter in word.lower() or guess_letter in word.upper():
        print("Yes, %s is in the word." % guess_letter)
        letters_guessed.append(guess_letter)
        blank[word.lower().index(guess_letter)] = word[word.lower().index(guess_letter)]

    guesses = 0
