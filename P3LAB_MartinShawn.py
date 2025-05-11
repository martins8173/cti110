# Ask user for amount
amount = float(input("Enter the amount of money (e.g., 4.99): "))

# Convert to cents
cents = int(round(amount * 100))

# Start breaking it down
output = ""

# Dollars
dollars = cents // 100
cents -= dollars * 100
if dollars == 1:
    output += "1 dollar\n"
elif dollars > 1:
    output += f"{dollars} dollars\n"

# Quarters
quarters = cents // 25
cents -= quarters * 25
if quarters == 1:
    output += "1 quarter\n"
elif quarters > 1:
    output += f"{quarters} quarters\n"

# Dimes
dimes = cents // 10
cents -= dimes * 10
if dimes == 1:
    output += "1 dime\n"
elif dimes > 1:
    output += f"{dimes} dimes\n"

# Nickels
nickels = cents // 5
cents -= nickels * 5
if nickels == 1:
    output += "1 nickel\n"
elif nickels > 1:
    output += f"{nickels} nickels\n"

# Pennies
pennies = cents
if pennies == 1:
    output += "1 penny\n"
elif pennies > 1:
    output += f"{pennies} pennies\n"

# Display result
print("\nMost efficient change:")
print(output.strip())
