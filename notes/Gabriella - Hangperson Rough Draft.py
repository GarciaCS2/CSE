import random
word_num = random.randint(1, 20)
word = "Word?"
right_letter_count = 0
doubles = 0
word_kind = 0  # 1 means it is a noun, 2 means it is a verb not ending in "Ing",

# 3 means it is a name, 4 means it is and adjective.
# 5 makes it a special word. (Irregular word) 0 means I don't know.

# Choosing the word
if word_num == 1:
    word = "cat"
    word_kind = 1
elif word_num == 2:
    word = "boxen"
    word_kind = 5
elif word_num == 3:
    word = "school"
    word_kind = 1
    doubles = 1
elif word_num == 4:
    word = "edison"
    word_kind = 3
elif word_num == 5:
    word = "happy"
    word_kind = 4
    doubles = 1
elif word_num == 6:
    word = "donut"
    word_kind = 1
elif word_num == 7:
    word = "travel"
    word_kind = 2
elif word_num == 8:
    word = "humor"
    word_kind = 1
elif word_num == 9:
    word = "cookie"
    word_kind = 1
    doubles = 1
elif word_num == 10:
    word = "awesome"
    word_kind = 4  #I left off on this here
    doubles = 1
elif word_num == 11:
    word = "america"
    doubles = 1
elif word_num == 12:
    word = "flannel"
    doubles = 2
elif word_num == 13:
    word = "zebra"
elif word_num == 14:
    word = "abracadabra"
    doubles = 5
elif word_num == 15:
    word = "python"
elif word_num == 16:
    word = "wiebe"
    doubles = 1
elif word_num == 17:
    word = "computer"
elif word_num == 18:
    word = "sunny"
    doubles = 1
elif word_num == 19:
    word = "number"
elif word_num == 20:
    word = "aerobic"


guesses = int(len(word)*2.5)

print("This word has %d letters." % len(word))

print()

# Hint!
hint = input("Want an extra hint?")

hint_type = random.randint(1, 4)

if hint == "yes" or "yes." or "Yes" or "YES" or "yeah" or "sure":
    if hint_type == 1:
        print("The word starts with " + word[0])
    elif hint_type == 2:
        print("The word ends in %s" % word[len(word)-1])
    elif hint_type == 3:
       print("This word is a %s" % )  #I left off on this.
    else:
        print("Actually, I changed my mind. You don't need a hint, right?")
else:
    print("Okay, then. Let's play")

print()

# Start Game
print("You have %s tries to find all the letters. Do not use caps. Use lowercase only." % guesses)
print("Some words may use letters twice. You only need to find one of each letter in the word.")
print("Each time you guess, a list of the letters you found will show up. Keep in mind:It is not in order.")
letters_required = len(word) - doubles
print()
print()

# Storing the letters
wrong_letters = ["in no order:"]
right_letters = [""]

# The game
while guesses > 0 and right_letter_count < letters_required:
    print()
    guess_letter = input("Give me a letter")
    if guess_letter in right_letters:
        print("Correct, but you already said that letter.")
    elif guess_letter in word:
        print("Yes, '%s' is in the word." % guess_letter)
        guesses = guesses - 1
        right_letter_count = right_letter_count + 1
        list.append(right_letters, guess_letter)
    elif guess_letter in wrong_letters:
        print("You already tried that letter.")
    else:
        print("No, sorry.")
        list.append(wrong_letters, guess_letter)
        guesses = guesses - 1
    print("%s tries left." % guesses)
    print("So far your correct letters are %s" % right_letters)


"""
    word.find(guess_letter)  # To print the letters that have been figured out so far. Incomplete.
"""

# Ending the game
print("Game end.")
print("The word was %s" % word)
if right_letter_count == letters_required:
    print("You won! You had %s guesses left." % guesses)
else:
    print("Try again next time.")


"""Links for help
https://www.google.com/search?rlz=1C1GCEA_enUS810US810&ei=EYDgW7W1Mqet0gLurqnYDg&q=how+to+check+if+a+string+doesn%27t+have+specific+characters+in+python&oq=how+to+check+if+a+string+doesn%27t+have+specific+characters+in+python&gs_l=psy-ab.3...6573.19624..19795...13.0..0.157.6847.42j32......0....1..gws-wiz.......0j0i71j0i67j0i22i30j0i13j0i13i30j33i299j33i22i29i30j33i160j33i10.W9XBMq2kLE0&safe=active&ssui=on
How to get certain character pos: https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
Print specific Character: https://stackoverflow.com/questions/35116496/python-print-specific-character-from-string
"""