print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
persons = int(input("How many people to split the bill? "))

total_tip = (tip_percent/100)*bill;
total_bill = bill + total_tip
bill_share = format(round(total_bill / persons, 2),".2f")

print(f"Each person should pay: ${bill_share}")