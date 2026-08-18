# grade_classifier.py

# Collect learner information
learner_name = input("Enter learner's name: ")
subject1 = float(input("Enter mark for Subject 1: "))
subject2 = float(input("Enter mark for Subject 2: "))
subject3 = float(input("Enter mark for Subject 3: "))

# Calculate the average
average = (subject1 + subject2 + subject3) / 3

# Assign letter grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Assign pass/fail status
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# Check for intervention
intervention = []

if subject1 < 40:
    intervention.append("Subject 1 needs intervention")

if subject2 < 40:
    intervention.append("Subject 2 needs intervention")

if subject3 < 40:
    intervention.append("Subject 3 needs intervention")

# Display report card
print("\n" + "=" * 45)
print("          STUDENT REPORT CARD")
print("=" * 45)
print(f"Learner Name : {learner_name}")
print(f"Subject 1    : {subject1:.2f}")
print(f"Subject 2    : {subject2:.2f}")
print(f"Subject 3    : {subject3:.2f}")
print(f"Average      : {average:.2f}")
print(f"Grade        : {grade}")
print(f"Status       : {status}")

print("\nIntervention:")
if intervention:
    for item in intervention:
        print(f"- {item}")
else:
    print("No intervention required.")

print("=" * 45)