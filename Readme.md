
# Expense Tracking System

## Project Overview
The **Expense Tracking System** is a command-line-based application designed to help users manage their personal finances. It enables users to track expenses, categorize transactions, and generate reports for better financial planning. The application uses SQLite for data storage, making it lightweight and easy to set up without external dependencies.

## Features

### 1. User Management
- Each user has a personal expense tracker, handled by the `User` class. The application allows for multiple users by storing each user's expenses in the SQLite database under their name.

### 2. Expense Tracking
- Users can add expenses categorized by pre-defined categories like "food", "transport", "utilities", etc., or create their own categories.
- Each expense consists of:
  - **Category**: A label such as "food" or "entertainment".
  - **Amount**: A positive float value representing the expense.
  - **Date**: The date of the transaction, formatted as `YYYY-MM-DD`.

### 3. Database Interaction (SQLite)
- All expenses are stored in an SQLite database (`expenses.db`), managed through functions in the `db_utils.py` file:
  - `save_transaction_to_db`: Saves new expenses.
  - `load_transactions_from_db`: Loads a user's transaction history.
  - `total_expenses`: Summarizes expenses for a specific month or year.
  - `categorize_expenses`: Summarizes total expenses per category for a user.

### 4. Report Generation
- Users can generate a report showing the total spending per category.
- The system also provides monthly or yearly summaries of expenses.

### 5. Input Validation
- The application ensures valid inputs for both amount and date.
  - **Amount**: Must be a positive value.
  - **Date**: Must be in `YYYY-MM-DD` format.

### 6. Command-Line Interface
- The interface provides the following options:
  - Add an expense.
  - View total expenses for a specific month or year.
  - Generate a categorized report of expenses.
  - Exit the application.

## File Structure
- **`db_utils.py`**: Handles database operations such as creating tables, saving transactions, and calculating summaries.
- **`expense.py`**: Defines the `Expense` class, which represents a single transaction and validates input.
- **`expenseTracker.py`**: Contains the `ExpenseTracker` class, which manages the user's categories and expenses.
- **`user.py`**: Contains the `User` class, responsible for associating a user with their personal expense tracker.
- **`main.py`**: The main entry point of the application, providing the command-line interface.
  
## How It Works
1. **Start**: The user enters their name, and the system loads their previous transactions from the SQLite database.
2. **Menu**: The user is presented with options to add an expense, view total expenses, generate a report, or exit.
3. **Add Expense**: The user selects a category or creates a new one, then inputs the amount and date of the expense.
4. **View Total Expenses**: The user can query total expenses for a specific month and year.
5. **Generate Report**: A breakdown of spending by category is displayed.

## Future Implementations
- **Expense Deletion/Editing**: Adding functionality to edit or delete past transactions.
- **Income Tracking**: Implementing features for income tracking, allowing users to compare income vs. expenses.
- **Data Export**: Providing the ability to export reports as CSV or PDF.
- **Budget Setting**: Allow users to set budgets for categories and notify them when they are close to exceeding those limits.
- **Multi-User Authentication**: Adding user authentication and password protection for security.

