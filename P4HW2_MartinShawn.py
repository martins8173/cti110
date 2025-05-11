#Shawn Martin

#3/30/25

#P3HW2

#Employee Pay Rates with Overtime

# This program calculates the gross pay of an employee based on regular and overtime hours worked.

# Initialize totals
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

while True:
    # Ask for employee name
    employee_name = input("Enter the name of the employee (or 'Done' to finish): ")

    # Sentinel value to stop the loop
    if employee_name.lower() == "done":
        break

    # Get hours worked and pay rate
    hours_worked = float(input(f"Enter the number of hours {employee_name} worked this week: "))
    pay_rate = float(input(f"Enter {employee_name}'s pay rate: "))

    # Determine regular and overtime hours
    regular_hours = 40
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40  # Keep regular hours fixed
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    # Calculate pay
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

    # Accumulate totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display individual employee results
    print("\n--- Employee Pay Summary ---")
    print("Employee Name:", employee_name)
    print("Pay Rate: ${:.2f}".format(pay_rate))
    print("Hours Worked: {:.2f}".format(hours_worked))
    print("Overtime Hours: {:.2f}".format(overtime_hours))
    print("Overtime Pay: ${:.2f}".format(overtime_pay))
    print("Regular Pay: ${:.2f}".format(regular_pay))
    print("Gross Pay: ${:.2f}".format(gross_pay))
    print("----------------------------\n")

# Display totals after loop ends
print("\n====== Payroll Summary ======")
print("Total number of employees:", employee_count)
print("Total Regular Pay: ${:.2f}".format(total_regular_pay))
print("Total Overtime Pay: ${:.2f}".format(total_overtime_pay))
print("Total Gross Pay: ${:.2f}".format(total_gross_pay))
print("=============================")
