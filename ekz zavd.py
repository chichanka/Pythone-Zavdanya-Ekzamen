import logging

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_file = "transactions.log"
            logging.basicConfig(filename=cls._instance.log_file, level=logging.INFO)
        return cls._instance

    def log(self, message):
        logging.info(message)

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.logger = Logger()

    def deposit(self, amount):
        self.balance += amount
        self.logger.log(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.logger.log(f"Withdrew {amount}. New balance: {self.balance}")

# Приклад використання
account = BankAccount("123456", 1000)
print(f"Initial balance: {account.balance}")

try:
    account.withdraw(500)
    account.deposit(200)
    account.withdraw(1000)
except ValueError as e:
    print(e)

with open(Logger()._instance.log_file, "r") as file:
    print("\nTransaction log:")
    print(file.read())
