class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(100)
account.withdraw(150)
print("Current Balance:", account.get_balance())
