import datetime
import math
# Easy Challenges.


def space(challenge_number):
    print()
    print("Challenge number %s." % challenge_number)


space(1)


def challenge1(first, last):  # 1
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


def challenge4(number):
    if number > 0:
        return "%s is positive" % number
    elif number == 0:
        return "%s is Zero." % number
    else:
        return "%s is negative." % number


print(challenge4(4))
print(challenge4(-4))
print(challenge4(0))
space(5)
# Medium Challenges


def challenge5(radius):  # pi r^2
    area = math.pi*(radius**2)  # fix this
    return "The area of such a circle is %s" % area


print(challenge5(5))
space(6)


def challenge6(radius):
    volume = (4/3)*(math.pi*(radius**3))
    return "The area of such a sphere is %s." % volume


print(challenge6(6))
space(7)


def challenge7(n):
    return n + n**2 + n**3


print(challenge7(7))
space(8)


def challenge8(f):  # test whether a number is within 150 of 2000 or 3000.
    number1 = 2000
    number2 = 3000
    if f <= number1 + 150 and f >= number1 - 150:
        return "%s is within 150 of 2000" % f
    elif f <= number2 + 150 and f >= number2 - 150:
        return "%s is within 150 of 3000" % f
    else:
        return "%s is not within 150 of 2000 nor 3000" % f


print(challenge8(2000-151))
print(challenge8(2000-150))
space(9)
# Harder Challenges


def challenge9(letter):
    if letter == "a" or "e" or "i" or "o" or "u":
        return "%s is a vowel." % letter
    else:
        return "%s is not a vowel." % letter


print(challenge9("a"))
space(10)


def challenge10(string):
    if string.isdigit():
        return "Yes, %s is numerical" % string
    else:
        return "No, %s is not numerical" % string


print(challenge10("apple"))
print(challenge10("10"))


def challenge11():
    time = datetime.datetime.now().time()
    print("The time is %s" % time)


challenge11()
space(12)


def challenge12(number, other_number):
    divi_1 = 1
    divisors_1 = []
    divisors_2 = []
    commons = []
    if number > other_number:
        range = int(number)
    elif number < other_number:
        range = int(other_number)
    for i in range(range):
        quo_1 = number/divi_1
        if quo_1 * divi_1 == number:
            list.append(divisors_1, divi_1)
        else:
            list.append(divisors_1, 0)
        quo_2 = number / divi_1
        if quo_2 * divi_1 == number:
            list.append(divisors_2, divi_1)
        else:
            list.append(divisors_1, 0)
    for i in range(range):
        if divisors_1[range] == divisors_2[range]:
            list.append(commons, divisors_1)
    return commons


print(challenge12(6, 9))

"""

12.	Write a Python program to find common divisors between two numbers in a given pair
"""
