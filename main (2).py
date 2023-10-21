class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number  # Private attribute
        self.__account_holder_name = account_holder_name  # Private attribute
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount

    def display_balance(self):
        return f"Account Number: {self.__account_number}, Holder Name: {self.__account_holder_name}, Balance: ${self.__account_balance}"

# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of the BankAccount
    account = BankAccount("12345", "John Doe", 1000.00)

    # Deposit and withdraw money
    account.deposit(500)
    account.withdraw(200)

    # Display the account balance
    print(account.display_balance())