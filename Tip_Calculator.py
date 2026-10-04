print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_per_person = (bill * (1 + tip / 100)) / people
final_amount = f"{bill_per_person:.2f}"
print(f"Each person should pay: ${final_amount}")