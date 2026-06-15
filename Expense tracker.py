import csv

FILE_NAME = "expenses.csv"

# Add expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    
    print("Expense added successfully!\n")

# Display all expenses
def display_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- Expense Records ---")
            for row in reader:
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: ₹{row[2]}")
    except FileNotFoundError:
        print("No expense records found.")
    print()

# Show summary
def show_summary():
    total = 0
    
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])

        print("\n--- Expense Summary ---")
        print(f"Total Expenses: ₹{total:.2f}\n")
    
    except FileNotFoundError:
        print("No expense records found.\n")

# Main menu
while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        display_expenses()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Try again.\n")