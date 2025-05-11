#Shawn Martin
#3/18/25
#P2HW2
#Lists and grading of tests



# Pseudocode:
# 1. Create a list to store grades for the 6 modules.
# 2. Prompt the user to enter grades for each of the 6 modules (Module 1 to Module 6).
# 3. Store the entered grades in the list.
# 4. Calculate the following:
#    - The lowest grade in the list.
#    - The highest grade in the list.
#    - The sum of all grades.
#    - The average of the grades (rounded to 2 decimal places).
# 5. Display the results in the required format:
#    - "Lowest grade: " followed by the lowest grade.
#    - "Highest grade: " followed by the highest grade.
#    - "Sum of grades: " followed by the sum of grades.
#    - "Average grade: " followed by the average grade with two decimal places.

grades = []

grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))  
grades.append(float(input("Enter grade for Module 3: ")))  
grades.append(float(input("Enter grade for Module 4: "))) 
grades.append(float(input("Enter grade for Module 5: ")))  
grades.append(float(input("Enter grade for Module 6: ")))

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Sum of grades: {sum_of_grades}")
print(f"Average grade: {average_grade:.2f}")
