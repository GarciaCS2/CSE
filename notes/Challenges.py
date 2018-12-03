# Easy Challenges.


def challenge1(first, last):  # 1
    print(last, first)


challenge1("Gabriella", "Garcia")


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


def challenge3(base, height):  # Challenge 3
    return (base * height)/2


print(challenge3(5, 8))


def challenge4(number):
    if number > 0:
        return "%s is positive" % number
    elif number == 0:
        return "%s is Zero." % number
    else:
        return "%s is negative." % number


print(challenge4(6))

# Medium Challenges


def challenge5()


# Harder Challenges


"""
Medium:
5.	Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output : 
r = 1.1
Area = 3.8013271108436504
6.	Write a Python program to get the volume of a sphere from a given radius.
7.	Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
8.	Write a Python program to test whether a number is within 150 of 2000 or 3000.

Hard:
9.	Write a Python program to test whether a passed letter is a vowel or not.
10.	Write a Python program to check if a string is numeric
11.	Write a Python program to get the system time
12.	Write a Python program to find common divisors between two numbers in a given pair
"""
