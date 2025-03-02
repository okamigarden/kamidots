# Calculator Program

def greet_guest():
    """Welcome the user."""
    print("Welcome to the Calculator")
    print("You can add, subtract, multiply, or divide two numbers.")

# Functions for arithmetic
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1 / num2

def main_menu():
    """Main menu for the calculator."""
    greet_guest()
    while True:
        print("\nOptions:")
        print("A. Add")
        print("S. Subtract")
        print("M. Multiply")
        print("D. Divide")
        print("Q. Quit")
        choice = input("Choose an option (A/S/M/D/Q): ").strip().upper()

        if choice in ["A", "S", "M", "D"]:
            handle_operation(choice)
        elif choice == "Q":
            print("Thanks for using the calculator!")
            break
        else:
            print("Invalid choice. Please select A, S, M, D, or Q.")

def handle_operation(choice):
    """Perform the chosen operation."""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == "A":
            print(f"Result: {add(num1, num2)}")
        elif choice == "S":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "M":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "D":
            print(f"Result: {divide(num1, num2)}")
    except ValueError:
        print("Invalid input. Please enter numbers.")

# Start the program
if __name__ == "__main__":
    main_menu()
