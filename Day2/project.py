print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: "))
tip = int(input("How much tip would you like to give? 10, 12 or 13 ?: "))
people = int(input("How many people to split the bill"))

tip_percent = tip /100
totatl_tip = tip * bill
total_bill = totatl_tip + bill
total_bill_per_people = total_bill/people

print(f"Each people should pay: {((tip/100)*bill+ bill)/people}")