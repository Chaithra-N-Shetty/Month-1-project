"""
Week 1 Python Project
"""

# -------------------------------
# 1. Temperature Converter
# -------------------------------
def temperature_converter():
    print("\n--- Temperature Converter ---")
   
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    choice = input("Convert (1) Celsius to Fahrenheit or (2) Fahrenheit to Celsius: ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print("Fahrenheit:", celsius_to_fahrenheit(c))

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Celsius:", fahrenheit_to_celsius(f))

    else:
        print("Invalid choice")


# -------------------------------
# 2. Simple Calculator
# -------------------------------
def calculator():
    print("\n--- Calculator ---")

    def add(a, b): return a + b
    def sub(a, b): return a - b
    def mul(a, b): return a * b
    def div(a, b): return a / b if b != 0 else "Cannot divide by zero"

    print("Operations: +, -, *, /")
    op = input("Enter operation: ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == "+":
        print("Result:", add(a, b))
    elif op == "-":
        print("Result:", sub(a, b))
    elif op == "*":
        print("Result:", mul(a, b))
    elif op == "/":
        print("Result:", div(a, b))
    else:
        print("Invalid operation")


# -------------------------------
# 3. Average Temperature Project
# -------------------------------
def average_temperature():
    print("\n--- Average Temperature Calculator ---")

    temperatures = []
    n = int(input("Enter number of days: "))

    for i in range(n):
        temp = float(input(f"Enter temperature for day {i+1}: "))
        temperatures.append(temp)

    avg = sum(temperatures) / len(temperatures)

    print("Temperatures:", temperatures)
    print("Average Temperature:", round(avg, 2))


# -------------------------------
# 4. NumPy Example
# -------------------------------
def numpy_example():
    print("\n--- NumPy Example ---")
    try:
        import numpy as np

        temps = np.array([30, 32, 31, 29, 35])
        print("Temperatures:", temps)
        print("Average:", np.mean(temps))
        print("Max:", np.max(temps))
        print("Min:", np.min(temps))

    except ImportError:
        print("NumPy not installed. Run: pip install numpy")


# -------------------------------
# 5. Pandas Example
# -------------------------------
def pandas_example():
    print("\n--- Pandas Example ---")
    try:
        import pandas as pd

        data = {
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
            "Temperature": [30, 32, 31, 29, 35]
        }

        df = pd.DataFrame(data)
        print(df)
        print("Average Temperature:", df["Temperature"].mean())

    except ImportError:
        print("Pandas not installed. Run: pip install pandas")


# -------------------------------
# 6. Visualization
# -------------------------------
def visualization():
    print("\n--- Temperature Visualization ---")
    try:
        import matplotlib.pyplot as plt

        days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        temps = [30, 32, 31, 29, 35]

        plt.plot(days, temps)
        plt.title("Temperature Trend")
        plt.xlabel("Days")
        plt.ylabel("Temperature")
        plt.show()

    except ImportError:
        print("Matplotlib not installed. Run: pip install matplotlib")


# -------------------------------
# Main Menu
# -------------------------------
def main():
    while True:
        print("\n====== Week 1 Python Project ======")
        print("1. Temperature Converter")
        print("2. Calculator")
        print("3. Average Temperature Project")
        print("4. NumPy Example")
        print("5. Pandas Example")
        print("6. Visualization")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            temperature_converter()
        elif choice == "2":
            calculator()
        elif choice == "3":
            average_temperature()
        elif choice == "4":
            numpy_example()
        elif choice == "5":
            pandas_example()
        elif choice == "6":
            visualization()
        elif choice == "7":
            print("Exiting project. Thank you!")
            break
        else:
            print("Invalid choice, try again.")


# Run program
if __name__ == "__main__":
    main()