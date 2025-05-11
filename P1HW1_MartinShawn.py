# Shawn Martin
# 3/2/25
# P1HW1
# A program for mathematical functions

base_value = input('Enter an integer as the base value:')
x = int(base_value)
exponent = input('Enter an integer as the exponent:')
y = int(exponent)
result = x  ** y
print(x, 'raised to the power of', y, 'is', result)


base_value = input('Enter a starting integer:')
x = int(base_value)
add = input('Enter an integer to add:')
y = int(add)
subtract = input('Enter an integer to subtract:')
z = int(subtract)
result = x + y - z
print(x, '+', y, '-', z, 'is equal to', result)
