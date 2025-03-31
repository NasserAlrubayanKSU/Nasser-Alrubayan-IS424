employee_salaries = {}

while True:
    name = input("Enter employee name (or 'no' to exit): ")

    if name.lower() == 'no':
        break

    while True:
        try:
            salary = float(input(f"Enter salary for {name}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for salary.")

    employee_salaries[name] = salary

print("\nEmployee Salary Dictionary:")
for name, salary in employee_salaries.items():
    print(f"{name}: ${salary:.2f}")