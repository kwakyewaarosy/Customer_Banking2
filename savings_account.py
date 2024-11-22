"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HEREsavings_account = Account(balance, interest_rate)


    # Calculate interest earned
     # ADD YOUR CODE HER monthly_interest_rate = interest_rate / 12
E

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HE interest_earned = (savings_account.balance * monthly_interest_rate * months) / 100
RE

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE Hsavings_account.set_balance(updated_balance)ERE

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE Hsavings_account.set_interest(interest_earned)ERE

    # Return the updated balance and interest earned.
    retuupdated_balance, interest_earned
rn  # ADD YOUR CODE Hif __name__ == "__main__":
   s
    balance = 1000
    interest_rate = PR)
    months = 12    thsnction
    updated_balance, interest_earned = create_savings_account(balance, interest_rate, monthsy results
    print(f"Updated Savings Account Balance: ${updated_balance:.2f}")
    print(f"Interest Earned: ${interest_ea
    Updated Savings Account Balance: $1060.00
    Interest Earned: $60.00rned:.2f}")ERE
