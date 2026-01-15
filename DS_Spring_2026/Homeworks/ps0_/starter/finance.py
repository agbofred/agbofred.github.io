########################################
# Name:
# Indicate any collaborators or tools used to assist you including AI:
# Estimated time spent (hrs):
########################################

"""
Problem 1: The Personal Finance Tracker (Procedural & Linear Collections)

This module provides functions to analyze monthly spending habits using
a procedural programming approach with linear collections (lists).
"""


def total_spending(transactions):
    """Returns the sum of all transaction amounts."""
    # TODO: Implement this function
    pass


def highest_expense(transactions):
    """Finds the maximum transaction value using traversal (not built-in max())."""
    # TODO: Implement this function
    pass


def filter_threshold(transactions, limit):
    """Returns transactions that exceed the specified limit."""
    # TODO: Implement this function
    pass


def main():
    """
    Tests the finance tracking functions with sample data.
    """
    # Sample transaction data
    transactions = [120.50, 45.75, 200.00, 35.20, 89.99, 150.00]
    
    print("Personal Finance Tracker")
    print("=" * 50)
    print(f"Transactions: {transactions}")
    print()
    
    # Test total_spending
    total = total_spending(transactions)
    print(f"Total Spending: ${total:.2f}")
    
    # Test highest_expense
    highest = highest_expense(transactions)
    print(f"Highest Expense: ${highest:.2f}")
    
    # Test filter_threshold
    threshold = 100.00
    high_expenses = filter_threshold(transactions, threshold)
    print(f"Expenses over ${threshold:.2f}: {high_expenses}")


if __name__ == "__main__":
    main()
