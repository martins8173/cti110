# Shawn Martin
# 3/18/25
# P2HW1
# Budgeting input (UPDATED)

destination = input('Enter a destination:')
budget = float(input('Enter your budget: $'))
gas = float(input('How much will you spend on gas?'))
accommodation = float(input('How much will you spend for accomodations?'))
food = float(input('How much will you spend for food?'))

total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses
print("\n--- Travel Budget Summary ---")
print(f"{'Destination:':<20}{destination}")
print(f"{'Budget:':<20}${budget:,.2f}")
print(f"{'Gas:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${accommodation:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print(f"{'Total:':<20}${total_expenses:,.2f}")
print(f"{'Remaining Budget:':<20}${remaining_budget:,.2f}")
