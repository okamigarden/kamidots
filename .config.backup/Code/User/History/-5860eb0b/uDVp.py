# Simple Calculator

# math functions
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

# the menu and perform calculations
def main_menu():
    print("Welcome to the Simple Calculator!")
    print("You can add, subtract, multiply, or divide two numbers.")

    while True:
        # Show menu options
        print("\nWEnter option")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
        
        # Get the user's choice
        choice = input("Enter the number: ")

        if choice == "5":
            break  # Exit the loop
        elif choice in ["1", "2", "3", "4"]:
            # Ask for two numbers
            while True:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    break  # Exit the loop if both inputs are valid
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            
            # Perform the operation
            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

# Step 3: Start the program
if __name__ == "__main__":
    main_menu()