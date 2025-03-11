#!/usr/bin/env python
# coding: utf-8

# # The Personal Budget Tracker
# 
# Create a simple finance tracker that records transactions as either income or expenses and calculates a summary of total income, total expenses, and the overall balance. The tracker should allow the user to continuously input transaction details until they decide to finish the session by entering 'done'. Each transaction requires the user to specify the type (income or expense) and the amount. The application should not accept any other transaction types besides these two. After all transactions have been entered, the tracker should compute and display the total income, total expenses, and the current balance, which is the difference between total income and total expenses.
# 
# ## Task:
# 1. add_transaction(amount, transaction_type): Implement this function to append a new transaction to the global `transactions` list. Each transaction is stored as a dictionary with two keys: `'amount'`, which stores a float representing the transaction amount, and `'type'`, which stores a string indicating whether the transaction is an 'income' or an 'expense'. Use `transactions.append()` to add the new transaction.
# 
# 2. calculate_summary(): This function calculates the total income, total expenses, and the balance from the transactions recorded in the `transactions` list. Iterate over `transactions` to separate incomes and expenses based on their `'type'`. Use a loop or list comprehensions to sum up the amounts for incomes and expenses separately. Calculate the balance by subtracting the total expenses from the total income. Return these three values (total income, total expenses, balance) at the end of the function.

# In[6]:


# Initialize a list to store transactions
global transactions
transactions = []

# Function to add a transaction
def add_transaction(amount, transaction_type):
    global transactions
    # TODO: Implement this function to append a new transaction to the transactions list
    # The transaction should be a dictionary with 'amount' and 'type' as keys
    pass

# Function to calculate summary
def calculate_summary():
    global transactions
    # TODO: Implement this function to calculate and return total income, total expenses, and balance
    # Hint: You can iterate over the transactions list and use a conditional to separate income and expenses
    return 0, 0, 0  # Replace these zeros with the actual calculated values of total_income, total_expenses, balance

# Main loop to record transactions
while True:
    transaction_type = input("Enter transaction type (income/expense) or 'done' to finish: ").lower()
    if transaction_type == 'done':
        break
    elif transaction_type not in ['income', 'expense']:
        print("Invalid transaction type. Please enter 'income', 'expense', or 'done'.")
        continue

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("The amount must be greater than 0.")
    except ValueError as e:
        print(f"Invalid amount: {e}")
        continue

    add_transaction(amount, transaction_type)

# Display summary
# TODO: After implementing the calculate_summary function, ensure this part calls it correctly and displays the output
print("Total Income: Placeholder")
print("Total Expenses: Placeholder")
print("Balance: Placeholder")


# In[ ]:




