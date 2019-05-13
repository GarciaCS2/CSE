import csv

# Find out which one item brings the most profit.
with open("Sales_Records.csv", 'r') as oldie_csv:  # The 'R' stands for "Read" mode, and the permissions to read it.
    reader = csv.reader(oldie_csv)
    data = {}
    print("DATA COMPILATION IN PROGRESS...")
    for row in reader:
        if not row[11] == 'Total Revenue':
            item_type = row[2]  # Compare ratios of Revenue/Amount Sold
            # print(item_type, ", REVENUE:", row[11], "of UNITS SOLD:", row[8])
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
                data[item_type]["BENEFIT_INDEX"] = data[item_type]["REVENUE"] / data[item_type]["UNITS_SOLD"]
            except KeyError:
                print()
                print(item_type)
                data[item_type] = {"NAME": item_type, "REVENUE": float(row[11]), "UNITS_SOLD": int(row[8]),
                                   "BENEFIT_INDEX": (float(row[11]) / float(row[8]))}
    print()
    print("MOVING ON TO DATA CALCULATION.")
    top_benefit_item = data[item_type]
    for item in data:
        if data[item]["BENEFIT_INDEX"] > top_benefit_item["BENEFIT_INDEX"]:
            print(data[item]["NAME"], "with BENEFIT INDEX:", data[item]["BENEFIT_INDEX"], "is better than:",
                  top_benefit_item["NAME"], "with BENEFIT INDEX:", top_benefit_item["BENEFIT_INDEX"])
            top_benefit_item = data[item]
    print("Finished!")
    print("The best item to sell is...")
    print(top_benefit_item["NAME"], "is the BEST item to sell with BENEFIT INDEX", top_benefit_item["BENEFIT_INDEX"],
          ", selling", top_benefit_item["UNITS_SOLD"], "units for a total of", top_benefit_item["REVENUE"])
