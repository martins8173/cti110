# Shawn Martin
# 3/2/25
# P1HW2
# Budgeting input

budget = int(input('Enter your budget:'))
destination = input('Enter a destination:')
gas = int(input('How much will you spend on gas?'))
accomodation = int(input('How much will you spend for accomodations?'))
food = int(input('How much will you spend for food?'))

print('Location:', destination)
print('Initial Budget:', budget)

print('Fuel:', gas)
print('Accomodations:', accomodation)
print('Food:', food)

result = budget - gas - accomodation - food
print('Remaining Balance:', result)
