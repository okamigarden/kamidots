# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:30:28 2024

@author: S23230140
"""

# Simple Calculator program

# Step 1: Define math functions
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

# Step 2: Show the main menu to the user
def main_menu():
    print("Calculator")
    print("This calculator can add, subtract, multiply, or divide two numbers.")
    
    while True:  # Keep showing the menu until the user chooses to quit
        print("\nSelect a function")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Quit")
        
        choice = input("Enter the number of your choice: ").strip()
        
        if choice == "1":
            print("\nAdding two numbers:")
            while True:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    break  # Break out of the loop if input is valid
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            print(f"The result is: {add(num1, num2)}")
            
        elif choice == "2":
            print("\nSubtracting two numbers:")
            while True:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    break  # Break out of the loop if input is valid
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            print(f"The result is: {subtract(num1, num2)}")
            
        elif choice == "3":
            print("\nMultiplying two numbers:")
            while True:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    break  # Break out of the loop if input is valid
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            print(f"The result is: {multiply(num1, num2)}")
            
        elif choice == "4":
            print("\nDividing two numbers:")
            while True:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    break  # Break out of the loop if input is valid
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            print(f"The result is: {divide(num1, num2)}")
            
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Step 3: Start the program
if __name__ == "__main__":
    main_menu()
