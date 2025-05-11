#Shawn Martin
#04/19/25
#P5 LAB
#Self Checkout change return

import random

def disperse_change(change):
    # Convert change to cents to avoid floating point issues
    cents = round(change * 100)

    # Coin values in cents
    dollar = 100
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    # Calculate the number of each coin
    dollars = cents // dollar
    cents %= dollar

    quarters = cents // quarter
    cents %= quarter

    dimes = cents // dime
    cents %= dime

    nickels = cents // nickel
    cents %= nickel

    pennies = cents // penny

    # Display change breakdown
    print("Change to be given:")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

def main():
    # Generate a random amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Amount owed: ${amount_owed:.2f}")

    # Prompt user for payment
    amount_paid = float(input("Enter the amount of cash you are putting into the machine: $"))

    # Calculate change
    if amount_paid < amount_owed:
        print("Not enough money inserted.")
    else:
        change = round(amount_paid - amount_owed, 2)
        print(f"Change owed: ${change:.2f}")
        disperse_change(change)

# Call the main function
if __name__ == "__main__":
    main()
