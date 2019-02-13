import random
import string
import Deluxe_Guess_Game


# Hangman-Specific Variables
word_bank = ["Super", "Word", "Bow", "Read", "Maverick", "Awesome", "Trapdoor", "Pizzicato", "Embezzled", "Garnish",
             "Math", "Python", "Variable", "Concatenation", "Awesome.com", "Fjord", "Crypt", "Bagpipes", "Haiku",
             "Jazzy", "Banjo", "River", "Discombobulated", "Zippy", "Gazebo", "Intermediate", "Croquet", "Aerobics",
             "Gloves", "Cats vs. Dogs", "Hangman", "Leaflet", "Champagne", "Haircut", "Minimum", "Maximum", "Cat"
             "Anaerobic", "Mr.Mayonnaise", "Mc.Donald's", "Grue", "Alphabet"]  # The word bank!

phrases = ["This is a phrase.", "This phrase has letters.", "You're playing Hangman.", "Letter by letter...",
           "import random", "import string"]

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


points = 8


# HANGMAN
choose_game()


