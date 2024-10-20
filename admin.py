from admin_db_utils import view_all_users, view_user_expenses, delete_user, update_user_expense

class Admin:
    def __init__(self):
        self.admin_password = "admin123"  # Placeholder password

    def authenticate(self):
        """Simple password authentication for admin access."""
        password = input("Enter admin password: ")
        if password == self.admin_password:
            print("Admin access granted.")
            return True
        else:
            print("Incorrect password.")
            return False

    def admin_menu(self):
        """Admin menu for performing actions."""
        if not self.authenticate():
            return

        while True:
            print("\n--- Admin Menu ---")
            print("1. View All Users")
            print("2. View User Expenses")
            print("3. Update User Expense")
            print("4. Delete User")
            print("5. Exit")
            choice = input("Select an option (1-5): ")

            if choice == '1':
                users = view_all_users()
                if users:
                    print("\n--- All Users ---")
                    for user in users:
                        print(f"User: {user}")
                else:
                    print("No users found.")
                    
            elif choice == '2':
                user_name = input("Enter user name to view expenses: ")
                expenses = view_user_expenses(user_name)
                if expenses:
                    print(f"\n--- Expenses for {user_name} ---")
                    for expense in expenses:
                        print(f"ID: {expense[0]}, Category: {expense[1]}, Amount: Rs.{expense[2]:.2f}, Date: {expense[3]}")
                else:
                    print(f"No expenses found for user {user_name}.")

            elif choice == '3':
                user_name = input("Enter user name: ")
                expense_id = int(input("Enter expense ID to update: "))
                new_category = input("Enter new category (leave blank if unchanged): ")
                new_amount = input("Enter new amount (leave blank if unchanged): ")
                new_amount = float(new_amount) if new_amount else None
                new_date = input("Enter new date (YYYY-MM-DD, leave blank if unchanged): ")
                result = update_user_expense(user_name, expense_id, new_category, new_amount, new_date)
                print(result)
                
            elif choice == '4':
                user_name = input("Enter the user name to delete: ")
                result = delete_user(user_name)
                print(result)
                
            elif choice == '5':
                print("Exiting admin menu.")
                break

            else:
                print("Invalid choice. Try again.")

# Ensure you call the menu somewhere in your main application
if __name__ == "__main__":
    admin = Admin()
    admin.admin_menu()
