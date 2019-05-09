import csv

# Find out which one item brings the most profit.
with open("Sales_Records.csv", 'r') as oldie_csv:  # The 'R' stands for "Read" mode, and the permissions to read it.
    reader = csv.reader(oldie_csv)
    data = {}
    for row in reader:
        if not row[11] == 'Total Revenue':
            item_type = row[2]  # Compare ratios of Revenue/Amount Sold
            print(item_type, ", REVENUE:", row[11], "of UNITS SOLD:", row[8])
            """
            0 = Region
            1 = Country
            2 = Item Type  # FOCUS ON THIS.
            3 = Sales Chart
            4 = Order Priority
            5 = Order Date
            6 = Order ID
            7 = Ship Date
            8 = Units Sold  # FOCUS ON THIS TOO.
            9 = Unit Price
            10 = Unit Cost
            11 = Total Revenue  # FOCUS ON THIS AS WELL.
            12 = Total Cost
            13 = Total Profit
            """
            try:
                data[item_type]["REVENUE"] += float(row[11])
                data[item_type]["UNITS_SOLD"] += int(row[8])
            except KeyError:
                data[item_type] = {"REVENUE": float(row[11]), "UNITS_SOLD": int(row[8])}
