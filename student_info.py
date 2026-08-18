# student_info.py

# Collect user information
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

# Display greeting
full_name = f"{first_name} {surname}"
print(f"\nWelcome, {full_name}!")

# Display formatted profile card
print("\n" + "=" * 30)
print("      STUDENT PROFILE")
print("=" * 30)
print(f"Full Name        : {full_name}")
print(f"Name (UPPERCASE) : {full_name.upper()}")
print(f"Name (Title Case): {full_name.title()}")

# Calculate age in months
age_in_months = age * 12
print(f"Age              : {age} years")
print(f"Age in Months    : {age_in_months}")

# Round favourite number
rounded_number = round(favourite_number, 2)
print(f"Favourite Number : {rounded_number}")

# Display data types
print("\nData Types")
print("-" * 30)
print(f"First Name       : {type(first_name)}")
print(f"Surname          : {type(surname)}")
print(f"Age              : {type(age)}")
print(f"Favourite Number : {type(favourite_number)}")

print("=" * 30)