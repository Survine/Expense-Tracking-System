# main.py
from user import User
from datetime import datetime

def display_categories(categories):
    """Display available categories for the user."""
    print("Available categories:")
    for index, category in enumerate(categories):
        print(f"{index + 1}. {category}")
    print(f"{len(categories) + 1}. Create a new category")

def main():
    name = input("Enter your name: ")
    user = User(name)

    while True:
        print(f"\n--- {user.name}'s Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. Generate Expense Report")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            print("\n---------------------------------------")
            display_categories(user.tracker.categories)

            category_choice = input(f"Select a category (1-{len(user.tracker.categories) + 1}): ")
            if category_choice.isdigit() and 1 <= int(category_choice) <= len(user.tracker.categories):
                category = user.tracker.categories[int(category_choice) - 1]
            elif category_choice == str(len(user.tracker.categories) + 1):
                category = input("Enter new category name: ")
            else:
                print("Invalid choice. Please try again.")
                continue

            try:
                amount = float(input("Enter amount: "))
                date = input("Enter date (YYYY-MM-DD): ")
                user.add_expense_for_user(category, amount, date)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (1-12, or 0 for all months): "))
            total = user.tracker.get_total_expenses(month, year)
            print(f"Total expenses for {month}/{year}: Rs.{total:.2f}")

        elif choice == '3':
            user.generate_report_for_user()

        elif choice == '4':
            print(f"Exiting {user.name}'s Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
