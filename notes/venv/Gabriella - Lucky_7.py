import random
money = 15
dice1 = 0
dice2 = 0
sum = 0
bet = 1
turn = 1
round_in_progress = False
high_score = 0
best_round = 0
print("Here's the deal:You start with %s dollars." % money)
print("You place a bet, and then dice are rolled. The sum of both dice must equal 7 for you to win.")
print("If you win, you get your money back, plus an additional $4. Lose, and you lose that money.")
print()

# Game start
while money > 0 or round_in_progress:
    print("Round %s!" % turn)
    print("You have $%s" % money)
    print()
    bet = int(input("How much money do you propose? ($1 recommended)"))
    round_in_progres = True
    money = money - bet
    print("Allright, let's roll.")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("The dice has been rolled. First number is %s, second number is %s" % (dice1, dice2))
    sum = dice1 + dice2
    print("That's a sum of %s" % sum)
    if sum == 7:
        print("It's your lucky day! You get your money back plus $4!")
        money = money + bet + 4
    else:
        print("Aww...try again next time. You now have $%s left." % money)
    if money > high_score:
        high_score = money
        best_round = turn
    turn = turn+1
    print()
    print()

print("You lasted for %s rounds." % turn)
print("The most money you had was $%s on turn %s...and you lost it!" % (high_score, best_round))
print("You should know that gambling is a bad idea.")