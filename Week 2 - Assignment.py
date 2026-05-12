# ==========================================
# WEEK 2: Assignment
# ==========================================

# ------------------------
# FUNCTIONS
# ------------------------

def process_numbers(numbers):
    # Sum of squares
    sum_squares = sum([x**2 for x in numbers])

    # Even numbers
    evens = [x for x in numbers if x % 2 == 0]

    print("\n--- Number Processing ---")
    print("Sum of squares:", sum_squares)
    print("Even numbers:", evens)


def process_student():
    print("\n--- Student Data ---")
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks separated by space: ").split()))

    avg = sum(marks) / len(marks)
    print(f"Average marks of {name}: {avg}")


def demonstrate_tuple():
    print("\n--- Tuple Example ---")
    person = tuple(input("Enter name, age, role (comma separated): ").split(","))
    
    if len(person) == 3:
        name, age, role = person
        print("Tuple unpacking:", name.strip(), age.strip(), role.strip())
    else:
        print("Invalid input for tuple!")


def square(x):
    return x * x


def multiply(a, b):
    return (lambda x, y: x * y)(a, b)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def clean_data(data_list):
    return sorted(list(set([x.strip() for x in data_list if x.strip()])))


# ------------------------
# MAIN PROGRAM
# ------------------------

def main():
    print("===== WEEK 2 APPLICATION =====")

    # LIST + FUNCTIONS
    numbers = list(map(int, input("\nEnter numbers separated by space: ").split()))
    process_numbers(numbers)

    # TUPLE
    demonstrate_tuple()

    # DICTIONARY (Student)
    process_student()

    # SET (duplicates removal demo)
    print("\n--- Set Example ---")
    sample = list(map(int, input("Enter numbers to remove duplicates: ").split()))
    print("Unique values:", set(sample))

    # FUNCTION
    print("\n--- Function Example ---")
    num = int(input("Enter number to square: "))
    print("Square:", square(num))

    # LAMBDA
    print("\n--- Lambda Example ---")
    a, b = map(int, input("Enter two numbers for multiplication: ").split())
    print("Multiply:", multiply(a, b))

    # RECURSION
    print("\n--- Recursion Example ---")
    n = int(input("Enter number for factorial: "))
    print("Factorial:", factorial(n))

    # DATA CLEANING PROJECT
    print("\n--- Data Cleaning Project ---")
    raw_data = input("Enter items (comma separated): ").split(",")
    print("Cleaned Data:", clean_data(raw_data))


# Run program
if __name__ == "__main__":
    main()