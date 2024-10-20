import sqlite3

DB_FILE = "expenses.db"

def view_all_users():
    """View all distinct users from the expenses table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT user FROM expenses")  # Get distinct users from the expenses table
    users = cursor.fetchall()
    conn.close()

    if users:
        return [user[0] for user in users]
    else:
        return []

def view_user_expenses(user_name):
    """View all expenses for a specific user."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, category, amount, date FROM expenses WHERE user = ?", (user_name,))
    expenses = cursor.fetchall()
    conn.close()

    return expenses

def delete_user(user_name):
    """Delete a user and their expenses."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Delete user's expenses from the expenses table
    cursor.execute("DELETE FROM expenses WHERE user = ?", (user_name,))
    
    conn.commit()
    conn.close()
    return f"User {user_name} and all their data deleted."

def update_user_expense(user_name, expense_id, new_category=None, new_amount=None, new_date=None):
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
    return f"Updated expense {expense_id} for user {user_name}."
