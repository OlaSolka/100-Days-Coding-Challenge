# Tip calculator
print("Welcome to the tip calculator! ")
bill = float(input("What was your total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? "))
result = round((bill + (bill*tip/100))/people, 2)
# How to round the value to second decimal place.
result = "{:.2f}".format(result)
# You have to make it as a string in this particular format: {:.2f} so it always is rounded,
# even if there's none or one digit after the coma.
print(f"Each person should pay {result}")
