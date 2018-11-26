import random

word = "Hi"  # Setting up the first variables
right_letter_count = 0
letters_required = 1
print(word)
counted_letters = []
doubles = 0
guesses = 0

# Choosing the word
word_bank = ["cat", "boxen", "edison", "donut", "zebra", "travel", "humor", "python", "computer",
             "number", "aerobic", "math", "cow", "dog", "snow", "cake", "glados", "cough", "list",
             "binary", "code", "person", "nice", "word", "time", "space", "github", "mouse", "dig",
             "dug", "string", "four", "cookies", "america", "moo", "yahoo", "wiebe", "goofy", "biology",
             "program", "update", "bee", "cake", "charm", "hangman", "hangwoman", "turkey",
             "thanksgiving", "halloween", "talk", "cast", "friday", "shop", "ballpark", "lines",
             "true", "false", "amazing"]
word = random.choice(word_bank)

# humor - *****
# humor - ***o*

# Figuring out how to detect doubles
for i in range(len(word)):
    count = word.count(word[i])
    if word[i] in counted_letters:
        guesses = guesses - 1
    elif count > 1:
        count = count - 1
        doubles = doubles + count
    list.append(counted_letters, word[i])

letters_required = len(word) - doubles

guesses = int(len(word)*2.5)

print("This word has %d letters." % len(word))

print()


# Hint!
hint = input("Want an extra hint?")

hint_type = random.randint(1, 4)

if hint.lower() in ["yes", "yes.", "yeah", "sure"]:
    if hint_type == 1:
        print("The word starts with " + word[0])
    elif hint_type == 2:
        print("The word ends in %s" % word[len(word)-1])
    elif hint_type == 3:
        if doubles > 0:
            print("This word has doubles. It uses one or more letter twice.")
        else:
            print("This word does not use doubles. It does not use any letters twice.")
    else:
        print("Actually, I changed my mind. You don't need a hint, right?")
else:
    print("Okay, then. Let's play")

print()

# Introduce Game
print("You have %s tries to find all the letters." % guesses)
print("Each time you guess, a list of the letters you found will show up.")

print()
print()

letter_pos = 0


# Storing the letters
wrong_letters = ["in no order:"]
right_letters = []
right_letter_list = []
for i in range(len(word)):
    list.append(right_letter_list, "*")

# Playing the Game

while guesses > 0 and right_letter_count < letters_required:
    print()
    guess_letter = input("Give me a letter")
    if guess_letter.lower() in right_letters:
        print("Correct, but you already said that letter.")
    elif guess_letter == "":
        print("What? I can't hear you.")
    elif guess_letter in word:
        print("Yes, '%s' is in the word." % guess_letter)
        guesses = guesses - 1
        right_letter_count = right_letter_count + 1
        letter_pos = word.index(guess_letter)
        right_letters.insert(letter_pos, guess_letter)
    elif guess_letter in wrong_letters:
        print("You already tried that letter.")
    else:
        print("No, sorry.")
        list.append(wrong_letters, guess_letter)
        guesses = guesses - 1
    print("%s tries left." % guesses)
    print()
    for i in range(len(word)):
        if (word[i]) in right_letters:
            right_letter_list[i] = word[i]  # Fix this

    print(right_letter_list)
    print()

# Ending the game
print("Game end.")
print("The word was %s" % word)
if right_letter_count == letters_required:
    print("You won! You had %s guesses left." % guesses)
else:
    print("Try again next time.")
