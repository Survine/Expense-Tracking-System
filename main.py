import sqlite3

DB_FILE = "expenses.db"

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

    def view_all_users(self):
        """View all distinct users from the expenses table."""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT user FROM expenses")  # Get distinct users from the expenses table
        users = cursor.fetchall()
        conn.close()

        if users:
            print("\n--- All Users ---")
            for user in users:
                print(f"User: {user[0]}")  # Display each distinct user
        else:
            print("No users found.")

    def view_user_expenses(self, user_name):
        """View all expenses for a specific user."""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, category, amount, date FROM expenses WHERE user = ?", (user_name,))
        expenses = cursor.fetchall()
        conn.close()

        if expenses:
            print(f"\n--- Expenses for {user_name} ---")
            for expense in expenses:
                print(f"ID: {expense[0]}, Category: {expense[1]}, Amount: Rs.{expense[2]:.2f}, Date: {expense[3]}")
        else:
            print(f"No expenses found for user {user_name}.")

    def delete_user(self, user_name):
        """Delete a user and their expenses."""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Delete user's expenses from the expenses table
        cursor.execute("DELETE FROM expenses WHERE user = ?", (user_name,))
        
        conn.commit()
        conn.close()
        print(f"User {user_name} and all their data deleted.")

    def update_user_expense(self, user_name, expense_id, new_category=None, new_amount=None, new_date=None):
        """Update a specific user's expense."""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Update the expense details
        if new_category:
            cursor.execute("UPDATE expenses SET category = ? WHERE id = ? AND user = ?", (new_category, expense_id, user_name))
        if new_amount:
            cursor.execute("UPDATE expenses SET amount = ? WHERE id = ? AND user = ?", (new_amount, expense_id, user_name))
        if new_date:
            cursor.execute("UPDATE expenses SET date = ? WHERE id = ? AND user = ?", (new_date, expense_id, user_name))
        
        conn.commit()
        conn.close()
        print(f"Updated expense {expense_id} for user {user_name}.")

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
                self.view_all_users()
            elif choice == '2':
                user_name = input("Enter user name to view expenses: ")
                self.view_user_expenses(user_name)
            elif choice == '3':
                user_name = input("Enter user name: ")
                expense_id = int(input("Enter expense ID to update: "))
                new_category = input("Enter new category (leave blank if unchanged): ")
                new_amount = input("Enter new amount (leave blank if unchanged): ")
                new_amount = float(new_amount) if new_amount else None
                new_date = input("Enter new date (YYYY-MM-DD, leave blank if unchanged): ")
                self.update_user_expense(user_name, expense_id, new_category, new_amount, new_date)
            elif choice == '4':
                user_name = input("Enter the user name to delete: ")
                self.delete_user(user_name)
            elif choice == '5':
                print("Exiting admin menu.")
                break
            else:
                print("Invalid choice. Try again.")

# Ensure you call the menu somewhere in your main application
if __name__ == "__main__":
    admin = Admin()
    admin.admin_menu()
