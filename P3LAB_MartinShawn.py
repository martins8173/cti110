def calculate_coins(amount):
    """
    Calculates the minimum number of coins needed to make change for a given amount.

    Args:
        amount: A float representing the amount of money (e.g., 2.73).

    Returns:
        None (prints the results to the console).
    """

    # Convert the amount to cents (integer)
    total_cents = int(amount * 100)

    # Calculate the number of each type of coin
    dollars = total_cents // 100
    total_cents %= 100
    quarters = total_cents // 25
    total_cents %= 25
    dimes = total_cents // 10
    total_cents %= 10
    nickels = total_cents // 5
    total_cents %= 5
    pennies = total_cents

    # Print the results
    if dollars > 0:
        print(f"{dollars} {'dollar' if dollars == 1 else 'dollars'}")
    if quarters > 0:
        print(f"{quarters} {'quarter' if quarters == 1 else 'quarters'}")
    if dimes > 0:
        print(f"{dimes} {'dime' if dimes == 1 else 'dimes'}")
    if nickels > 0:
        print(f"{nickels} {'nickel' if nickels == 1 else 'nickels'}")
    if pennies > 0:
        print(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")

# Get input from the user
amount = float(input("Enter the amount of money (e.g., 2.73): "))

# Call the function to calculate and print the results
calculate_coins(amount)
