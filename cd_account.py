"""Import the Account class from the Account.py file."""
# ADD YOUR CO
from Account import Account
)()
()

DE HERE

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the  
account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and in
     cd_account = Account(balance, interest_rate)
terest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE

    # Calculate interest earned
    # monthly_interest_rate = interest_rate / 12
interest_earned = (cd_account.balance * monthly_interest_rate * months) / 100
ADD YOUR CODE HERE

    # Update the CD account balance by adding the interest earned
    #   updated_balance = cd_account.balance + interest_earned
 ADD YOUR CODE HERE

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
      cd_account.set_balance(updated_balance)
    cd_account.set_interest(interest_earned)# ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and intereupdated_balance, interest_earned # ADD YOUR CODE HERE
