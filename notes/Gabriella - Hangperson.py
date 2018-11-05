import random
word_num = random.randint(1, 14)
word = "Word?"

# Choosing the word
if word_num == 1:
    word = "Cat"
elif word_num == 2:
    word = "Boxen"
elif word_num == 3:
    word = "School"
elif word_num == 4:
    word = "Edison"
elif word_num == 5:
    word = "Happy"
elif word_num == 6:
    word = "Donut"
elif word_num == 7:
    word = "Travel"
elif word_num == 8:
    word = "Humor"
elif word_num == 9:
    word = "Cookie"
elif word_num == 10:
    word = "Awesome"
elif word_num == 11:
    word = "America"
elif word_num == 12:
    word = "Flannel"
elif word_num == 13:
    word = "Zebra"
elif word_num == 14:
    word = "Abracadabra"
elif word_num == 15:
    word = "Python"
elif word_num == 16:
    word = "Wiebe"
elif word_num == 17:
    word = "Computer"
elif word_num == 18:
    word = "Sunny"

guesses = int(len(word)*1.5)

print("This word has %d letters." % len(word))

print("You have %s tries to find all the letters." % guesses)

print()
print()

wrong_letters = ["string"]
right_letters = ["string"]
while guesses > 0:
    print()
    guess_letter = input("Give me a letter")
    if guess_letter in right_letters:
        print("Correct, but you already said that letter.")
    elif guess_letter in word:
        print("Yes, '%s' is in the word." % guess_letter)
        guesses = guesses - 1
        list.append(right_letters, guess_letter)
    elif guess_letter in wrong_letters:
        print("You already tried that letter.")
    else:
        print("No, sorry.")
        list.append(wrong_letters, guess_letter)
        guesses = guesses - 1
    print("%s tries left." % guesses)

    word.find(guess_letter) # To print the letters that have been figured out so far. Incomplete.

print("Game end.")


"""Links for help
https://www.google.com/search?rlz=1C1GCEA_enUS810US810&ei=EYDgW7W1Mqet0gLurqnYDg&q=how+to+check+if+a+string+doesn%27t+have+specific+characters+in+python&oq=how+to+check+if+a+string+doesn%27t+have+specific+characters+in+python&gs_l=psy-ab.3...6573.19624..19795...13.0..0.157.6847.42j32......0....1..gws-wiz.......0j0i71j0i67j0i22i30j0i13j0i13i30j33i299j33i22i29i30j33i160j33i10.W9XBMq2kLE0&safe=active&ssui=on
How to get certain character pos: https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
Print specific Character: https://stackoverflow.com/questions/35116496/python-print-specific-character-from-string
"""