import random

word = "Hi"  # Setting up the first variables
right_letter_count = 0
letters_required = 1
print(word)
counted_letters = []
doubles = 0
guesses = 0

# Setup
language = int(input("Please select a language. 1 is for English, 2 is for Spanish."))

# Choosing the word
word_bank_english = ["cat", "boxen", "edison", "donut", "zebra", "travel", "humor", "python", "computer",
             "number", "aerobic", "math", "cow", "dog", "snow", "cake", "glados", "cough", "list",
             "binary", "code", "person", "nice", "word", "time", "space", "github", "mouse", "dig",
             "dug", "string", "four", "cookies", "america", "moo", "yahoo", "wiebe", "goofy", "biology",
             "program", "update", "bee", "cake", "charm", "hangman", "hangwoman", "turkey",
             "thanksgiving", "halloween", "talk"]

word_bank_spanish = ["gato", "mesa", "edison", "pan", "perro", "juegar", "humor", "python", "computadora",
             "nombre", "gimnasio", "matematicas", "cow", "fresa", "nieve", "ciudad", "glados", "chamara", "ser",
             "binary", "code", "persona", "bueno", "palabra", "tiempo", "geografia", "github", "caminar", "cerca",
             "estar", "cinturon", "cuatro", "galletas", "americano", "moo", "yahoo", "wiebe", "comico", "biologia",
             "program", "tomar", "tocar", "pastel", "chaqueta", "hombre", "mujer", "jamon",
             "navidad", "halloween", "hablar"]

if language == 1:
    word = random.choice(word_bank_english)
elif language == 2:
    word = random.choice(word_bank_spanish)

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

if language == 1:
    print("This word has %d letters." % len(word))

print()


# Hint!
if language == 1:
    hint = input("Want an extra hint?")
elif language == 2:
    hint = input("Quieres insinuación? (Escribes en el Espanol.)")

hint_type = random.randint(1, 4)

if language == 1:
    if hint.lower() in ["yes", "yes.", "yeah", "sure"]:
        if hint_type == 1:
            print("The word starts with " + word[0])
        elif hint_type == 2:
            print("The word ends in %s" % word[len(word)-1])
        elif hint_type == 3:
            if doubles > 0:
                print("This word has doubles.")
            else:
                print("This word does not use doubles.")
        elif hint_type == 4:
            print("Actually, I changed my mind. You don't need a hint, right?")
        else:
            print("Okay, then. Let's play")
elif language == 2:
    if hint.lower() in ["si", "si.", "quiero", "si, me quiero insunuación"]:
        if hint_type == 1:
            print("La palabra comienza en " + word[0])
        elif hint_type == 2:
            print("La palabra termina en %s" % word[len(word)-1])
        elif hint_type == 3:
            if doubles > 0:
                print("La palabra tiene dobles.")
            else:
                print("La palabra no tiene dobles. It does not use any letters twice.")
        elif hint_type == 4:
            print("Ah, no importa.")
    else:
            print("Vamanos!")

print()

# Introduce Game
if language == 1:
    print("You have %s tries to find all the letters." % guesses)
    print("Each time you guess, a list of the letters you found will show up.")
elif language == 2:
    print("Tienes %s adivinas para encontrar todos las letras." % guesses)

print()
print()

letter_pos = 0


# Storing the letters
wrong_letters = ["in no order:"]
right_letters = []


# Playing the Game

if language == 1:
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
        print("So far your correct letters are %s" % right_letters)
        print()
        for i in range(len(word)):
            if (word[i]) in right_letters:
                print(word[i])
            else:
                print("BLANK")
        print()
elif language == 2:
    while guesses > 0 and right_letter_count < letters_required:
        print()
        guess_letter = input("Tienes un letra?")
        if guess_letter.lower() in right_letters:
            print("Correcto, pero tu ya tiene la letra")
        elif guess_letter == "":
            print("Que? No escucho.")
        elif guess_letter in word:
            print("Si, '%s' esta en la palabra." % guess_letter)
            guesses = guesses - 1
            right_letter_count = right_letter_count + 1
            letter_pos = word.index(guess_letter)
            right_letters.insert(letter_pos, guess_letter)
        elif guess_letter in wrong_letters:
            print("Tu ya intentaste ese letra")
        else:
            print("No, lo siento.")
            list.append(wrong_letters, guess_letter)
            guesses = guesses - 1
        print("%s adivinas sobrante." % guesses)
        print("Tu tienes %s" % right_letters)
        print()
        for i in range(len(word)):
            if (word[i]) in right_letters:
                print(word[i])
            else:
                print("BLANK")
        print()

# Ending the game
if language == 1:
    print("Game end.")
    print("The word was %s" % word)
    if right_letter_count == letters_required:
        print("You won! You had %s guesses left." % guesses)
    else:
        print("Try again next time.")
elif language == 2:
    print("Juego terminado")
    print("La palabra es %s" % word)
    if right_letter_count == letters_required:
        print("Tu won! con %s adivinas sobrante." % guesses)
    else:
        print("Trataras otra vez.")