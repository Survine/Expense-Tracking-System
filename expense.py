# expense.py
from datetime import datetime

class Expense:
    def __init__(self, category: str, amount: float, date: str):
        self.category = category
        self.amount = self.validate_amount(amount)
        self.date = self.validate_date(date)
    
    def validate_amount(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    
    def validate_date(self, date: str) -> str:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in format YYYY-MM-DD")
        return date
