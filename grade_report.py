# List of student dictionaries
students = [
    {"name": "Alice", "maths": 85, "english": 78, "science": 90},
    {"name": "Brian", "maths": 65, "english": 70, "science": 68},
    {"name": "Cindy", "maths": 45, "english": 55, "science": 50},
    {"name": "David", "maths": 30, "english": 42, "science": 38},
    {"name": "Emma", "maths": 95, "english": 88, "science": 91}
]

# List to store processed results
results = []

# Variables for class statistics
total_average = 0
highest_average = 0
lowest_average = 100

# Process each student
for student in students:
    average = (student["maths"] + student["english"] + student["science"]) / 3

    # Determine grade
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

    # Determine pass/fail status
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Store results
    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })

    # Update class statistics
    total_average += average

    if average > highest_average:
        highest_average = average

    if average < lowest_average:
        lowest_average = average

# Calculate class average
class_average = total_average / len(results)

# Display class report
print("\n" + "=" * 65)
print("                     CLASS REPORT")
print("=" * 65)
print(f"{'Name':<15}{'Average':<12}{'Grade':<10}{'Status':<10}")
print("-" * 65)

for result in results:
    print(f"{result['name']:<15}{result['average']:<12.2f}{result['grade']:<10}{result['status']:<10}")

print("=" * 65)
print(f"Class Average : {class_average:.2f}")
print(f"Highest Average: {highest_average:.2f}")
print(f"Lowest Average : {lowest_average:.2f}")
print("=" * 65)

# Search functionality
while True:
    search = input("\nEnter a student name to search (or type 'exit' to quit): ").strip()

    if search.lower() == "exit":
        print("Exiting program...")
        break

    found = False

    for result in results:
        if result["name"].lower() == search.lower():
            print("\nStudent Found")
            print("-" * 30)
            print(f"Name   : {result['name']}")
            print(f"Average: {result['average']:.2f}")
            print(f"Grade  : {result['grade']}")
            print(f"Status : {result['status']}")
            found = True
            break

    if not found:
        print("Student not found.")