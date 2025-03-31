numbers = []

print("Enter 10 numbers:")
for i in range(10):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"\nThe list of numbers is: {numbers}")
print(f"The largest number in the list is: {largest}")