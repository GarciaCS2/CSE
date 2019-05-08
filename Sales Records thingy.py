import csv

with open("Sales_Records.csv", 'r') as oldie_csv:  # The 'R' stands for "Read" mode, and the permissions to read it.
    reader = csv.reader(oldie_csv)
    for row in reader:
        old_number = row[1]
        print(old_number)

