import csv


def even(number):  # FOR LUHN FORMULA
    if (number % 2) == 0:
        return True


def is_16_digits(num: str):
    if len(num) == 16:
        return True
    return False


def multiple_o_10(num: int):  # FOR LUHN FORMULA
    if num % 10 == 0:
        return True
    return False


def passed_luhn_test(num: str):  # LUHN FORMULA
    last_num = int(num[15])
    new_num = num[:14]  # CUT OFF
    new_num = new_num[::-1]  # REVERSE
    number = list(new_num)  # ODD DIGITS PART A
    for i in range(len(number)):
        if even(i):
            new_digit = int(number[i])*2  # ODD DIGITS PART B (MULTIPLY by 2)
            if new_digit > 9:  # ODD DIGITS PART C 1 (CHECK OVER 9)
                new_digit -= 9  # ODD DIGITS PART C 2 (SUBTRACT 9)
            number[i] = str(new_digit)
    total_sum = 0
    for j in range(len(number)):
        total_sum += int(number[j])
    if multiple_o_10((total_sum + last_num)):
        return True
    return False


def validate_card_number(num: str):
    if not is_16_digits(num):
        # print("NON-16 DIGITS FOUND")
        return False
    if not passed_luhn_test(num):
        # print("LUHN TEST FAILED!")
        return False
    return True


with open("Book1.csv", 'r') as old_csv:  # The 'R' stands for "Read" mode, and the permissions to read it.
    # with open("ValidNumbers.csv", 'w', newline='') as new_csv:
    #     print("Writing file...  ")
    #     reader = csv.reader(old_csv)
    #     writer = csv.writer(new_csv)
    #     print("Processing...")
    #     for row in reader:
    #         old_number = row[0]
    #         if validate_card_number(old_number):
    #             writer.writerow(row)
    with open("InvalidNumbers.csv", 'w', newline='') as new_csv:
        print("Writing file...  ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            old_number = row[0]
            if not validate_card_number(old_number):
                writer.writerow(row)
    print("Done")


