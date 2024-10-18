from expenseTracker import ExpenseTracker

class User:
    """Represents a user with a personal expense tracker."""
    def __init__(self, name: str):
        self.name = name
        # The ExpenseTracker will handle loading and saving expenses for this user
        self.tracker = ExpenseTracker(self.name)

    def get_user_expenses(self):
        """Get total expenses tracked by this user."""
        return self.tracker.expenses

    def add_expense_for_user(self, category: str, amount: float, date: str):
        """Add expense for the current user."""
        self.tracker.add_expense(category, amount, date)
    
    def generate_report_for_user(self):
        """Generate expense report for the current user."""
        self.tracker.generate_report()
    
    def export_report_for_user(self):
        """Export the user's expense report to a CSV file."""
        self.tracker.export_report_to_csv()
