import csv


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

with open("Book1.csv", 'r') as old_csv:  # The 'R' stands for "Read" mode, and the permissions to read it.
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file...  ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]
            first_num = int(old_number[0])
            if first_num % 2 == 0:
                writer.writerow(row)
            # print(int(old_number) + 1)
            # print(int(old_number) + 1)

print("OK")
