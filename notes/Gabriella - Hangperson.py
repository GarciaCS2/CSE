import random

word = "Hi"  # Setting up the first variables
right_letter_count = 0

print(word)

# Choosing the word
word_bank = ["cat", "boxen", "edison", "donut", "zebra", "travel", "humor", "python", "computer",
             "number", "aerobic", "math", "cow", "dog", "snow"]
word = (random.choice(word_bank))


guesses = int(len(word)*2.5)

print("This word has %d letters." % len(word))

print()


# Hint!
hint = input("Want an extra hint?")

hint_type = random.randint(1, 3)

if hint == "yes" or "yes." or "Yes" or "YES" or "yeah" or "sure":
    if hint_type == 1:
        print("The word starts with " + word[0])
    elif hint_type == 2:
        print("The word ends in %s" % word[len(word)-1])
    else:
        print("Actually, I changed my mind. You don't need a hint, right?")
else:
    print("Okay, then. Let's play")

print()

# Introduce Game
print("You have %s tries to find all the letters. Do not use caps. Use lowercase only." % guesses)
print("Each time you guess, a list of the letters you found will show up.")
print("If you guess later letters in the word earlier, the lits of letters may get mixed up.")

letters_required = len(word)

print()
print()

letter_pos = 0


# Storing the letters
wrong_letters = ["in no order:"]
right_letters = []


# Playing the Game

while guesses > 0 and right_letter_count < letters_required:
    print()
    guess_letter = input("Give me a letter")
    if guess_letter in right_letters:
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
    print("So far your correct letters are %s" % right_letters)


# Ending the game
print("Game end.")
print("The word was %s" % word)
if right_letter_count == letters_required:
    print("You won! You had %s guesses left." % guesses)
else:
    print("Try again next time.")
