# expenseTracker.py
from db_utils import ensure_db_exists, load_transactions_from_db, save_transaction_to_db, total_expenses, categorize_expenses
from expense import Expense

class ExpenseTracker:
    DEFAULT_CATEGORIES = ["food", "transport", "utilities", "entertainment", "other"]

    def __init__(self, user_name: str):
        self.user_name = user_name
        self.categories = self.DEFAULT_CATEGORIES[:]
        ensure_db_exists()  # Ensure the DB exists when creating a tracker

    def load_transactions(self):
        """Load expenses from the database."""
        expenses = load_transactions_from_db(self.user_name)
        # Add any custom categories the user has
        for expense in expenses:
            if expense.category not in self.categories:
                self.categories.append(expense.category)
        return expenses

    def add_category(self, category: str):
        """Add a new category if it doesn't exist."""
        if category not in self.categories:
            self.categories.append(category)

    def add_expense(self, category: str, amount: float, date: str):
        """Add a new expense and save it."""
        if category not in self.categories:
            self.add_category(category)

        try:
            expense = Expense(category, amount, date)
            save_transaction_to_db(self.user_name, expense)
            print(f"Expense added: {expense.category}, ${expense.amount:.2f}, {expense.date}")
        except ValueError as e:
            print(f"Error adding expense: {e}")

    def get_total_expenses(self, month: int, year: int) -> float:
        """Calculate total expenses for a given month and year."""
        return total_expenses(self.user_name, month, year)

    def generate_report(self):
        """Generate and print the expense report by category."""
        category_totals = categorize_expenses(self.user_name)
        print("\nExpense Report:")
        for category, total in category_totals.items():
            print(f"{category.capitalize()}: ${total:.2f}")
