while True:
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

fahrenheit = (9/5) * celsius + 32

# Display the result
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")