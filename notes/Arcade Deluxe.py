import random
import string
points = 8
# Command banks
name = input("What is your username?")

cancel_items = ["cancel", "never mind", "nevermind", "go back"]
show_stats_items = ["show", "stats", "show stats"]
print("Welcome to the Arcade!")

def show_stats():
    print(name.upper())
    print("You have %s points" % points)



def command():
    do = input("Type in a command")
    if do in cancel_items:
        print("Ok, back to game.")
    elif do in show_stats_items:
        show_stats


def choose_game():
    print("Your choices are: Hangman, Lucky 7's, Guess Game,")
    choice = input("Which game would you like to play? ")

# HANGMAN
word_bank = ["Super", "Word", "Bow", "Read", "Maverick", "Awesome", "Trapdoor", "Pizzicato", "Embezzled", "Garnish",
             "Math", "Python", "Variable", "Concatenation", "Awesome.com", "Fjord", "Crypt", "Bagpipes", "Haiku",
             "Jazzy", "Banjo", "River", "Discombobulated", "Zippy", "Gazebo", "Intermediate", "Croquet", "Aerobics",
             "Gloves", "Cats vs. Dogs", "Hangman", "Leaflet", "Champagne", "Haircut", "Minimum", "Maximum", "Cat"
             "Anaerobic", "Mr.Mayonnaise", "Mc.Donald's", "Grue", "import random", "Alphabet"]  # The word bank!

#  Setting up variables
word = random.choice(word_bank)
word_lower = list(word.lower())
letters_guessed = []
blank = []
punctuation_with_space = list(string.punctuation)
punctuation_with_space.append(" ")
win = False
letters = 0
for i in range(len(word)):
    if word[i] in list(string.ascii_letters):
        letters += 1

print("This word has %s letters" % letters)
for i in range(len(word)):
    blank.append("_")  # Assemble list

# Playing
while points > 0 and not win:
    print()
    print(letters_guessed)
    print("You have %s guesses." % points)
    guess_letter = input("Give me a letter:")
    if guess_letter.lower() in letters_guessed:
        print("You have already guessed '%s'." % guess_letter)
    elif guess_letter.lower() in word.lower():
        print("Yes, %s is in the word." % guess_letter)
        letters_guessed.append(guess_letter.lower())  # Add to guessed Letter list
    elif guess_letter not in word.lower() or guess_letter not in word.upper():  # Wrong guess
        print("No, %s is not in the word. Sorry!" % guess_letter)
        letters_guessed.append(guess_letter.lower())
        points -= 1
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

print("The word was %s!" % word)
if win:
    print("You won! You had %s guesses left!" % points)
else:
    print("You lost. Try again next time.")
