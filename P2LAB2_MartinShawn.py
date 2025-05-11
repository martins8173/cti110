#Shawn Martin
#3/18/25
#P2LAB2
#Assignment tests student's knowledge of how to write code that uses a dictionary to store user input and displays output to the user

my_dict = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

keys = my_dict.keys()

print("Available vehicles:", keys)

vehicle = input("Enter the vehicle model (exactly as shown above): ")

if vehicle in my_dict:
    mpg = my_dict[vehicle]
    print(f"The MPG for the {vehicle} is {mpg}.")


    miles = float(input("Enter the number of miles you plan to drive: "))


    gallons_needed = miles / mpg


    print(f"Gallons of gas needed: {gallons_needed:.2f}")
else:
    print("Vehicle not found. Please enter a valid vehicle name from the list.")
