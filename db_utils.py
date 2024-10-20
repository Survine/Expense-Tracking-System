import sqlite3
from collections import defaultdict
from expense import Expense

DB_FILE = "expenses.db"

def ensure_db_exists():
    """Ensure that the SQLite database and necessary tables exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create the expenses table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def load_transactions_from_db(user_name: str):
    """Load expenses from the SQLite database for a given user."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Retrieve all expenses for the current user
    cursor.execute("SELECT category, amount, date FROM expenses WHERE user = ?", (user_name,))
    rows = cursor.fetchall()
    conn.close()

    # Populate the user's expenses
    expenses = []
    for row in rows:
        category, amount, date = row
        expenses.append(Expense(category, float(amount), date))
    
    return expenses

def save_transaction_to_db(user_name: str, expense: Expense):
    """Save a new expense to the SQLite database with the user's name."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Insert the new expense into the database
    cursor.execute(
        "INSERT INTO expenses (user, category, amount, date) VALUES (?, ?, ?, ?)",
        (user_name, expense.category, expense.amount, expense.date)
    )
    
    conn.commit()
    conn.close()

def total_expenses(user_name: str, month: int, year: int) -> float:
    """Calculate total expenses for a given month and year.
       If month is 0, sum all expenses for the entire year.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    if month == 0:
        # Query to sum all expenses for the given year, ignoring the month
        cursor.execute("""
            SELECT SUM(amount) FROM expenses 
            WHERE user = ? AND strftime('%Y', date) = ?
        """, (user_name, str(year)))
    else:
        # Query to sum expenses for a specific month and year
        cursor.execute("""
            SELECT SUM(amount) FROM expenses 
            WHERE user = ? AND strftime('%Y', date) = ? AND strftime('%m', date) = ?
        """, (user_name, str(year), str(month).zfill(2)))

    total = cursor.fetchone()[0] or 0.0
    conn.close()
    return total

def categorize_expenses(user_name: str) -> dict:
    """Categorize expenses and calculate total for each category."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Query to sum expenses for each category for the current user
    cursor.execute("""
        SELECT category, SUM(amount) FROM expenses 
        WHERE user = ? 
        GROUP BY category
    """, (user_name,))
    
    rows = cursor.fetchall()
    conn.close()

    # Create a dictionary of category totals
    category_totals = {category: total for category, total in rows}
    return category_totals
