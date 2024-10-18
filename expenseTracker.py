import csv
from collections import defaultdict
from datetime import datetime
from expense import Expense

class ExpenseTracker:
    DEFAULT_CATEGORIES = ["food", "transport", "utilities", "entertainment", "other"]
    CSV_FILE = "expenses.csv"
    REPORT_FILE = "expense_report.csv"

    def __init__(self, user_name: str):
        self.user_name = user_name  # Store the user's name
        self.expenses = []
        self.categories = self.DEFAULT_CATEGORIES[:]
        self.ensure_csv_file_exists()  # Ensure the CSV file is ready with correct headers
        self.load_transactions_from_csv()

    def ensure_csv_file_exists(self):
        """Ensure that the CSV file exists with headers."""
        try:
            with open(self.CSV_FILE, mode='r', newline='') as file:
                reader = csv.reader(file)
                headers = next(reader, None)  # Check if there's a header
                if headers != ["User", "Category", "Amount", "Date"]:
                    raise ValueError("Incorrect CSV format. Expected headers not found.")
        except (FileNotFoundError, ValueError):
            # Create the file with headers if it doesn't exist or is incorrectly formatted
            with open(self.CSV_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["User", "Category", "Amount", "Date"])  # Write the headers
            print(f"New CSV file '{self.CSV_FILE}' created with correct headers.")

    def load_transactions_from_csv(self):
        """Load expenses from the CSV file and filter by the current user."""
        try:
            with open(self.CSV_FILE, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    if row:
                        user_name, category, amount, date = row
                        if user_name == self.user_name:  # Load only this user's expenses
                            self.expenses.append(Expense(category, float(amount), date))
                            if category not in self.categories:
                                self.categories.append(category)
        except FileNotFoundError:
            print(f"'{self.CSV_FILE}' not found. A new file will be created on the first save.")
        except csv.Error:
            print(f"Error reading CSV file '{self.CSV_FILE}'. Please check the file format.")

    def save_transaction_to_csv(self, expense: Expense):
        """Save a new expense to the shared CSV file with the user's name."""
        with open(self.CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.user_name, expense.category, expense.amount, expense.date])

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
            self.expenses.append(expense)
            self.save_transaction_to_csv(expense)
            print(f"Expense added: {expense.category}, ${expense.amount:.2f}, {expense.date}")
        except ValueError as e:
            print(f"Error adding expense: {e}")

    def total_expenses(self, month: int, year: int) -> float:
        """Calculate total expenses for a given month and year."""
        total = 0.0
        for expense in self.expenses:
            expense_date = datetime.strptime(expense.date, "%Y-%m-%d")
            if (month == 0 or expense_date.month == month) and expense_date.year == year:
                total += expense.amount
        return total

    def categorize_expenses(self) -> dict:
        """Categorize expenses and calculate total for each category."""
        category_totals = defaultdict(float)
        for expense in self.expenses:
            category_totals[expense.category] += expense.amount
        return dict(category_totals)

    def generate_report(self):
        """Generate and print the expense report by category."""
        category_totals = self.categorize_expenses()
        print("\nExpense Report:")
        for category, total in category_totals.items():
            print(f"{category.capitalize()}: ${total:.2f}")

    def export_report_to_csv(self):
        """Export the expense report by category to a CSV file."""
        category_totals = self.categorize_expenses()
        with open(self.REPORT_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Total Amount"])
            for category, total in category_totals.items():
                writer.writerow([category.capitalize(), f"${total:.2f}"])
        print(f"Expense report exported to {self.REPORT_FILE}")
