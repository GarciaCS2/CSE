import csv


def divisible_by_3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


def all_16(num: str):
    length = len(num)
    if length == 16:
        return True
    print("NOT EVERY NUMBER IS 16 DIGITS!!!")
    return False


def validate(num: str):
    if not all_16(num):
        return False
    if not divisible_by_2(num):
        return False
    if not divisible_by_3(num):
        return False
    return True


# with open("Book1.csv", 'r') as old_csv:  # The 'R' stands for "Read" mode, and the permissions to read it.
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print("Writing file...  ")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#             old_number = row[0]
#             new_number = int(old_number) + 1
#             row[0] = new_number
#             writer.writerow(row)
#             print(int(old_number) + 1)
#             print(int(old_number) + 1)

#print("OK")

# with open("Book1.csv", 'r') as old_csv:  # The 'R' stands for "Read" mode, and the permissions to read it.
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print("Writing file...  ")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#         for row in reader:
#             old_number = row[0]
#             first_num = int(old_number[0])
#             if first_num % 2 == 0:
#                 writer.writerow(row)
#     print("Done")
#             # print(int(old_number) + 1)
#             # print(int(old_number) + 1)
#
# print("OK")

def reverse_it(string):
    txt = "Hello World"[::-1]
    print(txt)


reverse_it("Hello World")


with open("Book1.csv", 'r') as old_csv:  # The 'R' stands for "Read" mode, and the permissions to read it.
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file...  ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
    print("Done")

            # print(int(old_number) + 1)
            # print(int(old_number) + 1)

print("OK")


def valid_card_number(num:str):
    ??????


print(valid_card_number("7891283560948756"))

list_num - list(number)
for index in range(len(list_num)):
    list_num[index] = int(list_num[index])