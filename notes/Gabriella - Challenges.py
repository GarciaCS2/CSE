import datetime
import math
# Easy Challenges.


def space(challenge_number):
    print()
    print("Challenge number %s." % challenge_number)


space(1)


def challenge1(first, last):  # Challenge 1
    print(last, first)


challenge1("Gabriella", "Garcia")
space(2)


def challenge2(number):  # Challenge 2
    factor = 0
    product = 0
    while factor < number and not product == number:
        factor = factor + 1
        product = factor * 2
    if product == number:
        return "%s is even" % number
    else:
        return "%s is not even" % number


print(challenge2(700))
space(3)


def challenge3(base, height):  # Challenge 3
    return (base * height)/2


print(challenge3(5, 8))
space(4)


def challenge4(number):    # Challenge 4
    if number > 0:
        return "%s is positive" % number
    elif number == 0:
        return "%s is Zero." % number
    else:
        return "%s is negative." % number


print(challenge4(4))
print(challenge4(-4))
print(challenge4(0))
print()
space(5)
# Medium Challenges


def challenge5(radius):  # pi r^2
    area = math.pi*(radius**2)    # Challenge 5
    return "The area of such a circle is %s" % area


print(challenge5(5))
space(6)


def challenge6(radius):  # Challenge 6
    volume = (4/3)*(math.pi*(radius**3))
    return "The area of such a sphere is %s." % volume


print(challenge6(6))
space(7)


def challenge7(n):   # Challenge 7
    return n + n**2 + n**3


print(challenge7(7))
space(8)


def challenge8(f):  # test whether a number is within 150 of 2000 or 3000. Challenge 8
    number1 = 2000
    number2 = 3000
    if number1 - 150 <= f <= number1 + 150:
        return "%s is within 150 of 2000" % f
    elif number2 - 150 <= f <= number2 + 150:
        return "%s is within 150 of 3000" % f
    else:
        return "%s is not within 150 of 2000 nor 3000" % f


print(challenge8(2000-151))
print(challenge8(2000-150))
print()
space(9)

# Harder Challenges


def challenge9(letter):    # Challenge 9
    if letter.isdigit():
        return "%s is not a vowel." % letter
    if letter == "a" or "e" or "i" or "o" or "u":
        return "%s is a vowel." % letter
    else:
        return "%s is not a vowel." % letter


print(challenge9("a"))

print(challenge9("2"))
space(10)


def challenge10(string):    # Challenge 10
    if string.isdigit():
        return "Yes, %s is numerical" % string
    else:
        return "No, %s is not numerical" % string


print(challenge10("apple"))
print(challenge10("10"))


def challenge11():    # Challenge 11
    time = datetime.datetime.now().time()
    print("The time is %s" % time)


challenge11()
space(12)


def challenge12(number, other_number):    # Challenge 12
    quotients_1 = []
    quotients_2 = []
    common_quotients = []
    for i in range(number):
        plus = i + 1
        quotients_1.append(number/plus)
    for j in range(other_number):
        plus = j + 1
        quotients_2.append(other_number/plus)
    for k in range(min(number, other_number)):
        if quotients_1[k] in quotients_2 and quotients_1[k] % 1 == 0:
            list.append(common_quotients, quotients_1[k])
    for i in range(len(common_quotients)):
        common_quotients[i] = int(common_quotients[i])
    return "The common divisors between %s and %s are %s." % (number, other_number, common_quotients)


print(challenge12(6, 9))
