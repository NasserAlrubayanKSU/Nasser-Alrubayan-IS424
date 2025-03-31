while True:
    try:
        number = int(input("Enter a number to see its multiplication table: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print(f"\nMultiplication Table for {number}:")
print("-" * 20)

for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")

print("-" * 20)