from datetime import datetime

class User:
    def __init__(self, name, password, tpin, accno):
        self.name = name
        self.password = password
        self.tpin = tpin
        self.accno = accno

    def authenticate(self, input_name, input_password, input_tpin, input_accno):
        if (input_name == self.name and
            input_password == self.password and
            input_tpin == self.tpin and
            input_accno == self.accno):
            print("Authentication successful! Go ahead.")
            return True
        else:
            print("Authentication failed. Check your credentials.")
            return False

class Account:
    def __init__(self, name, accno):
        self.name = name
        self.accno = accno
        self.balance_amount = 0  # Initialize balance amount to 0
        self.transactions = []   # List to store transaction objects

    def account_history(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)

    def process_transaction(self, transaction_type, amount, description):
        if transaction_type == "credit":
            self.balance_amount += amount
        elif transaction_type == "debit":
            if self.balance_amount >= amount:
                self.balance_amount -= amount
            else:
                print("Insufficient balance.")
                return
        else:
            print("Invalid transaction type.")
            return

        # Capture current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a Transaction object with timestamp and add it to transactions list
        transaction = Transaction(current_datetime, transaction_type, amount, description)
        self.transactions.append(transaction)
        print(f"Transaction ({transaction_type}): Amount {amount} {transaction_type}ed successfully.")

    def display_balance(self):
        print(f"Current Balance: {self.balance_amount}")

class Transaction:
    def __init__(self, timestamp, transaction_type, amount, description):
        self.timestamp = timestamp
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description

    def __repr__(self):
        return f"{self.timestamp} - {self.transaction_type}: {self.amount} ({self.description})"

class Budget:
    def __init__(self, daily_limit):
        self.daily_limit = daily_limit

    def set_daily_limit(self, new_limit):
        self.daily_limit = new_limit
        print(f"Daily budget limit updated to {self.daily_limit}.")

    def get_daily_limit(self):
        return self.daily_limit

def generate_financial_report(user_instance, account_instance, budget_instance):
    report = f"Financial Report\n\n"
    report += f"User Name: {user_instance.name}\n"
    report += f"Account Number: {user_instance.accno}\n"
    report += f"Daily Budget Limit: {budget_instance.get_daily_limit()}\n"
    report += f"Account Balance: {account_instance.balance_amount}\n"

    return report

if __name__ == "__main__":
    # Predefined user credentials
    name = "Prem"
    password = "2004"
    tpin = "1234"
    accno = "6374005564"

    # Create an instance of User
    user_instance = User(name, password, tpin, accno)

    # Simulate authentication
    input_name = input("Enter your name: ")
    input_password = input("Enter your password: ")
    input_tpin = input("Enter your tpin: ")
    input_accno = input("Enter your account number: ")

    if user_instance.authenticate(input_name, input_password, input_tpin, input_accno):
        # If authentication is successful, proceed with account operations
        account_instance = Account(name, accno)
        budget_instance = Budget(daily_limit=100000)  # Initialize daily budget limit

        while True:
            print("\nChoose operation:")
            print("1. View Account History")
            print("2. Perform Transaction")
            print("3. Account Balance")
            print("4. View Daily Budget Limit")
            print("5. Exit")
            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == "1":
                account_instance.account_history()
            elif choice == "2":
                transaction_type = input("Enter transaction type (credit/debit): ").lower()
                amount = float(input("Enter amount: "))
                description = input("Enter transaction description: ")
                account_instance.process_transaction(transaction_type, amount, description)
            elif choice == "3":
                account_instance.display_balance()
            elif choice == "4":
                print(f"Daily Budget Limit: {budget_instance.get_daily_limit()}")
            elif choice == "5":
                print("Generating financial report...")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

        # Generate and print financial report after exiting the loop
        report = generate_financial_report(user_instance, account_instance, budget_instance)
        print(report)
