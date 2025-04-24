# Empty list to store expenses
expenses = []


# Function to add a new expense
def add_expense():
    # Displaying message to user
    print("\n Add New Expense")
    # Taking item name as input from user
    item = input("Item name: ")
    try:
        # Taking amount spent as input and converting it to float
        amount = float(input("Amount spent (₹): "))
        # Adding the expense to the expenses list as a dictionary
        expenses.append({"item": item, "amount": amount})
        # Confirming that the expense was added successfully
        print(" Expense added successfully!")
    except ValueError:
        # In case of invalid input, showing error message
        print(" Invalid amount! Please enter a number.")


# Function to view all expenses
def view_expenses():
    # Checking if there are any expenses recorded
    print("\n Your Expenses:")
    if not expenses:
        # If no expenses recorded, displaying message
        print("No expenses recorded yet.")
    else:
        # Iterating through each expense and displaying it
        for i, exp in enumerate(expenses, 1):
            print(f"{i}. {exp['item']} - ₹{exp['amount']}")


# Function to view total expense
def total_expense():
    # Calculating the sum of all expenses
    total = sum(exp["amount"] for exp in expenses)
    # Displaying total expense to user
    print(f"\n Total Expense: ₹{total}")


# Function to edit an expense
def edit_expense():
    view_expenses()  # Displaying current expenses
    if not expenses:
        print("No expenses to edit.")
        return
    try:
        index = int(input("\nEnter the number of the expense to edit: ")) - 1
        if 0 <= index < len(expenses):
            # Taking new item name and amount from user
            item = input("New item name: ")
            amount = float(input("New amount spent (₹): "))
            # Updating the expense in the list
            expenses[index] = {"item": item, "amount": amount}
            print("Expense updated successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Function to delete an expense
def delete_expense():
    view_expenses()  # Displaying current expenses
    if not expenses:
        print("No expenses to delete.")
        return
    try:
        index = int(input("\nEnter the number of the expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            # Deleting the expense from the list
            del expenses[index]
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Main function to handle user choices
def main():
    # Running an infinite loop to display menu repeatedly
    while True:
        # Displaying options for the user
        print("\n Expense Tracker Menu:")
        print("1. Add Expense")  # Option to add a new expense
        print("2. View Expenses")  # Option to view all recorded expenses
        print("3. View Total")  # Option to view total expense
        print("4. Edit Expense")  # Option to edit an existing expense
        print("5. Delete Expense")  # Option to delete an expense
        print("6. Exit")  # Option to exit the program

        # Taking user's choice as input
        choice = input("Enter your choice (1-6): ")

        # Checking the user's choice and calling respective functions
        if choice == "1":
            add_expense()  # Call function to add expense
        elif choice == "2":
            view_expenses()  # Call function to view expenses
        elif choice == "3":
            total_expense()  # Call function to view total expense
        elif choice == "4":
            edit_expense()  # Call function to edit an expense
        elif choice == "5":
            delete_expense()  # Call function to delete an expense
        elif choice == "6":
            print("Exiting... Thank you!")
            break  # Break the loop and exit the program
        else:
            print("Invalid option. Please select a valid option between 1 and 6.")


# Calling the main function to start the program
if __name__ == "__main__":
    main()
