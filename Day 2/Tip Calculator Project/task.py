print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total = (bill + bill * (tip / 100)) / people
total_r = "{:.2f}".format(total)
print(f"Each person should pay {total_r}")