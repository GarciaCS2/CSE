import csv

with open("Sales Records.csv", 'r') as old_csv:  # The 'R' stands for "Read" mode, and the permissions to read it.
    reader = csv.reader(old_csv)
    for row in range(29):
        thingy = reader[row][0]
        print(thingy)
