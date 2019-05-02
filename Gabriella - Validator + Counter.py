import csv


def even(number):
    if (number % 2) == 0:
        return True


def is_16_digits(num: str):
    if len(num) == 16:
        return True
    return False


def cutoff_reverse(num: str):
    new_num = num[:14]
    new_num = new_num[::-1]
    return new_num


def passed_luhn_test(num: str):
    last_num = int(num[15])
    numbers = list(cutoff_reverse(num))
    for i in range(len(numbers)):
        if even(i):
            new_digit = int(numbers[i])*2
            if new_digit > 9:
                new_digit -= 9
            numbers[i] = str(new_digit)
    total_sum = 0
    for j in range(len(numbers)):
        total_sum += int(numbers[j])
    if not total_sum % 10 == last_num:
        return True
    return False


def validate_card_number(num: str, call_number: bool):
    if not is_16_digits(num):
        if call_number:
            print("NON-16 DIGITS FOUND")
            print(num, "IS NOT 16 DIGITS.")
        return False
    if not passed_luhn_test(num):
        if call_number:
            print("LUHN TEST FAILED!")
            print(num, "IS AN INVALID NUMBER!")
        return False
    return True


with open("Book1.csv", 'r') as old_csv:
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
        total_rows = 0
        invalid_rows = 0
        for row in reader:
            total_rows += 1
            old_number = row[0]
            if not validate_card_number(old_number, False):
                invalid_rows += 1
                writer.writerow(row)
        leftover_rows = total_rows - invalid_rows
    print()
    print("STATS:")
    print(invalid_rows, "of", total_rows, "invalid.")
    print(leftover_rows, "rows of", total_rows, "valid.")
    print("Done")

print()
print("FAKE VISA NUMBERS")
validate_card_number("4485765429615473", True)
validate_card_number("4556411150946563", True)
validate_card_number("4024007136575240206", True)
print()
print("FAKE")
