total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10,12 or 15?  "))
split_bill = int(input("How many people to split the bill?  "))
billwithtip = (total_bill * (1 + tip /100))
finale_bill = round((billwithtip / split_bill),2)
print(f"Bill for each person ${finale_bill}")