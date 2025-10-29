# Task 2: Using the Math Module for Calculations

import math

# Ask user for input
try:
    num = float(input("Enter a number: "))

    # Perform calculations
    sqrt_val = math.sqrt(num)
    log_val = math.log(num)
    sine_val = math.sin(num)

    # Display results
    print(f"\nResults for number {num}:")
    print(f"Square root: {sqrt_val}")
    print(f"Natural log: {log_val}")
    print(f"Sine (radians): {sine_val}")

except ValueError:
    print("Error: Please enter a valid positive number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
