# Collect user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

# Display results
print("\n" + "=" * 40)
print(f"{'Operation':<20}{'Result':>20}")
print("=" * 40)

print(f"{'Addition (+)':<20}{addition:>20.2f}")
print(f"{'Subtraction (-)':<20}{subtraction:>20.2f}")
print(f"{'Multiplication (*)':<20}{multiplication:>20.2f}")

# Handle division safely
if num2 != 0:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

    print(f"{'Division (/)':<20}{division:>20.2f}")
    print(f"{'Floor Division (//)':<20}{floor_division:>20.2f}")
    print(f"{'Modulus (%)':<20}{modulus:>20.2f}")
else:
    print(f"{'Division (/)':<20}{'Error: Cannot divide by zero':>20}")
    print(f"{'Floor Division (//)':<20}{'Error: Cannot divide by zero':>20}")
    print(f"{'Modulus (%)':<20}{'Error: Cannot divide by zero':>20}")

print("=" * 40)