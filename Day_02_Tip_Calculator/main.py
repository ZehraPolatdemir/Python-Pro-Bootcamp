print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15 "))

tip1 = (bill*tip)/100
tip2 = tip1 + bill
people = int(input("How many people to split the bill? "))
result = tip2/people
final_amount = round(result,2)

print("\n------ Bill Summary ------")
print("I hope you enjoyed your meal!")
print(f"Each person should pay: ${final_amount}")



