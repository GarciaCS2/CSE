import random
word_bank = ["Super", "Word", "Bow", "Read", "Maverick", "Awesome", "Trapdoor", "Pizzicato", "Embezzled", "Garnish",
             "Math", "Python", "Variable", "Concatenation", "Fjord", "Crypt", "Bagpipes", "Haiku", "Jazzy", "Banjo",
             "River", "Discombobulated", "Zippy", "Gazebo", "Intermediate", "Croquet", "Aerobics", "Anaerobic"]

word = random.choice(word_bank)
word_lower = list(word.lower())
letters_guessed = []
guesses = 8


case = "lower"
win = False

print("WORD = " + word + ", %s LETTERS" % len(word))
print("GUESSES = " + str(guesses))



while win == False and guesses > 0:
    print()
    print(letters_guessed)
    blank = ["_" * len(word)]
    guess_letter = input("Give me a letter:")
    if guess_letter.lower in letters_guessed:
        print("You have already guessed this letter.")
    elif guess_letter.lower() in word.lower():
        print("Yes, %s is in the word." % guess_letter)
        letters_guessed.append(guess_letter.lower())
        #  blank[(word.lower()).index(guess_letter.lower())] = word[(word.lower()).index(guess_letter.lower())]

        print(blank)
        for i in range(len(word)):
            if word_lower[i] in letters_guessed:
                blank[i] = word[i]
                print(blank)
            else:
                blank[i] = "_"
                print(blank)
        display = "".join(blank)
    elif guess_letter not in word.lower() or guess_letter not in word.upper():
        print("No, %s is not in the word. Sorry!" % guess_letter)
        letters_guessed.append(guess_letter.lower())
        guesses -= 1
    print(display)
