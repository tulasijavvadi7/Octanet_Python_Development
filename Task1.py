import datetime

class User:
    def __init__(self, user_id, pin, initial_balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = initial_balance
        self.transactions = []
        self.add_transaction(f"Account created with initial balance: ${initial_balance}")

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

class ATM:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self, user_id, pin, initial_balance):
        self.users[user_id] = User(user_id, pin, initial_balance)
        print(f"User {user_id} registered successfully with an initial balance of ${initial_balance}.")

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            self.current_user = self.users[user_id]
            return True
        return False

    def transaction_history(self):
        if self.current_user:
            print("\nTransaction History:")
            for transaction in self.current_user.transactions:
                print(transaction)
        else:
            print("No user authenticated.")

    def check_balance(self):
        if self.current_user:
            print(f"Current balance: ${self.current_user.balance}")
        else:
            print("No user authenticated.")

    def withdraw(self, amount):
        if self.current_user:
            if self.current_user.balance >= amount:
                self.current_user.balance -= amount
                transaction = f"{datetime.datetime.now()} - Withdrawn: ${amount}"
                self.current_user.add_transaction(transaction)
                print(f"Withdrawal successful. New balance: ${self.current_user.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("No user authenticated.")

    def deposit(self, amount):
        if self.current_user:
            self.current_user.balance += amount
            transaction = f"{datetime.datetime.now()} - Deposited: ${amount}"
            self.current_user.add_transaction(transaction)
            print(f"Deposit successful. New balance: ${self.current_user.balance}")
        else:
            print("No user authenticated.")

    def transfer(self, target_user_id, amount):
        if self.current_user:
            if target_user_id in self.users:
                if self.current_user.balance >= amount:
                    self.current_user.balance -= amount
                    self.users[target_user_id].balance += amount
                    transaction = f"{datetime.datetime.now()} - Transferred: ${amount} to User ID {target_user_id}"
                    self.current_user.add_transaction(transaction)
                    self.users[target_user_id].add_transaction(f"{datetime.datetime.now()} - Received: ${amount} from User ID {self.current_user.user_id}")
                    print(f"Transfer successful. New balance: ${self.current_user.balance}")
                else:
                    print("Insufficient balance.")
            else:
                print("Target user ID not found.")
        else:
            print("No user authenticated.")

    def quit(self):
        self.current_user = None
        print("User logged out.")

def main():
    atm = ATM()

    while True:
        print("\nWelcome to the ATM")
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter new user ID: ")
            pin = input("Enter new PIN: ")
            initial_balance = float(input("Enter initial balance: "))
            atm.add_user(user_id, pin, initial_balance)

        elif choice == "2":
            user_id = input("Enter user ID: ")
            pin = input("Enter PIN: ")

            if atm.authenticate_user(user_id, pin):
                print("Authentication successful.")
                while True:
                    print("\nATM Menu:")
                    print("1. Transaction History")
                    print("2. Check Balance")
                    print("3. Withdraw")
                    print("4. Deposit")
                    print("5. Transfer")
                    print("6. Quit")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        atm.transaction_history()
                    elif choice == "2":
                        atm.check_balance()
                    elif choice == "3":
                        amount = float(input("Enter amount to withdraw: "))
                        atm.withdraw(amount)
                    elif choice == "4":
                        amount = float(input("Enter amount to deposit: "))
                        atm.deposit(amount)
                    elif choice == "5":
                        target_user_id = input("Enter target user ID: ")
                        amount = float(input("Enter amount to transfer: "))
                        atm.transfer(target_user_id, amount)
                    elif choice == "6":
                        atm.quit()
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Authentication failed. Please try again.")

        elif choice == "3":
            print("Thank you, visit again!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
