from user import User
from datetime import datetime

def display_categories(categories):
    """Display available categories for the user."""
    print("Available categories:")
    for index, category in enumerate(categories):
        print(f"{index + 1}. {category}")
    print(f"{len(categories) + 1}. Create a new category")

def main():
    name = input("Enter your name: ")  # Ask user for their name
    user = User(name)  # Create a User object with their own expense tracker

    while True:
        print(f"\n--- {user.name}'s Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. Generate Expense Report")
        print("4. Export Report to CSV")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            # Adding an expense
            print("--------------------------------")
            print("Select a category:")
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
            # Viewing total expenses
            print("------------------------------------")
            print("1. Total expenses up to today")
            print("2. Yearly total expenses")
            print("3. Monthly total expenses")
            view_choice = input("Select an option (1-3): ")

            if view_choice == '1':
                total = user.tracker.total_expenses(datetime.now().month, datetime.now().year)
                print(f"Total expenses up to today: ${total:.2f}")
            elif view_choice == '2':
                year = int(input("Enter year (YYYY): "))
                total = user.tracker.total_expenses(0, year)
                print(f"Total expenses for {year}: ${total:.2f}")
            elif view_choice == '3':
                year = int(input("Enter year (YYYY): "))
                month = int(input("Enter month (1-12): "))
                total = user.tracker.total_expenses(month, year)
                print(f"Total expenses for {month}/{year}: ${total:.2f}")
            else:
                print("Invalid choice. Please try again.")

        elif choice == '3':
            # Generating the expense report
            user.generate_report_for_user()

        elif choice == '4':
            # Export the report to CSV
            user.export_report_for_user()

        elif choice == '5':
            print(f"Exiting {user.name}'s Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
