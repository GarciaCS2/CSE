import random
setup = [0, 1, 2, 3]
counted_letters = []  # 0 = right_letter_count, 1 = guesses, 2 = doubles, 3 = letters_required
word_bank = ["cat", "edison", "donut", "zebra", "travel", "humor", "python", "computer", "number", "aerobic",
             "math", "cow", "dog", "snow", "cake", "cough", "list", "binary", "code", "person", "nice", "amazing",
             "word", "time", "space", "github", "mouse", "dig", "dug", "string", "four", "cookies", "america", "moo",
             "goofy", "biology", "program", "update", "bee", "cake", "charm", "turkey", "thanksgiving", "halloween",
             "talk", "cast", "friday", "shop", "ballpark", "lines", "true", "false"]
word = random.choice(word_bank)  # Choosing the word
setup[1] = int(len(word)*2.5)
for i in range(len(word)):  # Figuring out how to detect doubles
    count = word.count(word[i])
    if word[i] in counted_letters:
        setup[1] = setup[1] - 1
    elif count > 1:
        count = count - 1
        setup[2] = setup[2] + count
    list.append(counted_letters, word[i])
setup[3] = len(word) - setup[2]
print("This word has %d letters. You have %s tries to find all the letters." % (len(word), setup[1]))  # Introduce Game
letter_pos = 0
wrong_letters = []  # Storing the letters
right_letters = []
right_letter_list = []
for i in range(len(word)):  # making the display list
    list.append(right_letter_list, "*")
while setup[1] > 0 and setup[0] < setup[3]:  # Playing the Game
    print()
    guess_letter = input("Give me a letter")
    if guess_letter.lower() in right_letters:
        print("Correct, but you already said that letter.")
    elif guess_letter == "":
        print("What? I can't hear you.")
    elif guess_letter in word:
        print("Yes, '%s' is in the word." % guess_letter)
        setup[1] = setup[1] - 1
        right_letter_count = setup[0] + 1
        right_letters.insert(0, guess_letter)
    elif guess_letter in wrong_letters:
        print("You already tried that letter.")
    else:
        print("No, sorry.")
        list.append(wrong_letters, guess_letter)
        setup[1] = setup[1] - 1
    print("%s tries left." % setup[1])
    for i in range(len(word)):
        if (word[i]) in right_letters:
            right_letter_list[i] = word[i]
    print(right_letter_list)
if setup[0] == setup[3]:
    print("Game end. You won! You had %s guesses left." % setup[1])
else:
    print("Game end. The word was %s. Try again next time." % word)
