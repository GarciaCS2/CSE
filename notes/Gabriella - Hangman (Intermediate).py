import random
import string
word_bank = ["Super", "Word", "Bow", "Read", "Maverick", "Awesome", "Trapdoor", "Pizzicato", "Embezzled", "Garnish",
             "Math", "Python", "Variable", "Concatenation", "Awesome.com", "Fjord", "Crypt", "Bagpipes", "Haiku",
             "Jazzy", "Banjo", "River", "Discombobulated", "Zippy", "Gazebo", "Intermediate", "Croquet", "Aerobics",
             "Meme", "Dream", "Zebra", "Quick", "The quick brown fox jumped over the lazy dog.", "What do you meme?"
             "Gloves", "Cats vs. Dogs", "Hangman", "Leaflet", "Champagne", "Haircut", "Minimum", "Maximum", "Cat",
             "Anaerobic", "Mr.Mayonnaise", "Mc.Donald's", "Grue", "import random", "Penultimate", "Practice", "How",
             "Alphabet", "Python notes", "Calibrate", "Font", "Where", "Who", "Why", "What", "When"]  # The word bank!

word = random.choice(word_bank)  #  Setting up variables
word_lower = list(word.lower())
letters_guessed = []
guesses = 8
blank = []
punctuation_with_space = list(string.punctuation)
punctuation_with_space.append(" ")
win = False
letters = 0
for i in range(len(word)):
    if word[i] in list(string.ascii_letters):
        letters += 1
print("This word has %s letters" % letters)
print("You have %s guesses." % guesses)
for i in range(len(word)):
    blank.append("_")  # Assemble list

while guesses > 0 and not win:  # Playing
    print()
    print(letters_guessed)
    print("You have %s guesses." % guesses)
    guess_letter = input("Give me a letter:")
    if guess_letter.lower() in letters_guessed:
        print("You have already guessed '%s'." % guess_letter)
    elif guess_letter.lower() in word.lower():
        print("Yes, %s is in the word." % guess_letter)
        letters_guessed.append(guess_letter.lower())  # Add to guessed Letter list
    elif guess_letter not in word.lower() or guess_letter not in word.upper():  # Wrong guess
        print("No, %s is not in the word. Sorry!" % guess_letter)
        letters_guessed.append(guess_letter.lower())
        guesses -= 1
    for i in range(len(word)):  # Assemble list again for display
        if word_lower[i] in letters_guessed:
            blank[i] = word[i]
        elif word_lower[i] in list(punctuation_with_space):  # Punctuation check
            blank[i] = word[i]
        else:  # Blanks
            blank[i] = "_"
    display = "".join(blank)  # Display
    print(display)
    if display == word:
        win = True
    print()

#  Did you win or lose?
print("The word was %s!" % word)
if win:
    print("You won! You had %s guesses left!" % guesses)
else:
    print("You lost. Try again next time.")
