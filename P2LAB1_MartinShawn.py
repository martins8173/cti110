# Shawn Martin
# 03/18/25
# P2Lab1
# Assignment tests student's knowledge of how to write code that performs mathematical calculations and displays information to users


import math

# Get radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display the results with the specified formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
