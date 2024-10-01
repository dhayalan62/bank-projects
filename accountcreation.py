class BankAccount:
    def __init__(self, name, address, mobile, father_name, aadhar, occupation):
        self.name = name
        self.address = address
        self.mobile = mobile
        self.father_name = father_name
        self.aadhar = aadhar
        self.occupation = occupation
        self.account_number = self.generate_account_number()

    # Function to generate a random account number
    @staticmethod
    def generate_account_number():
        import random
        return str(random.randint(1000000000, 9999999999))

    # Display account information
    def display_account_info(self):
        print("\nAccount Information:")
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Mobile Number: {self.mobile}")
        print(f"Father's Name: {self.father_name}")
        print(f"Aadhar Card Number: {self.aadhar}")
        print(f"Occupation: {self.occupation}")
        print("-" * 40)

# Function to create a new account
def create_account():
    print("Enter the following details to create a new bank account:")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    mobile = input("Enter your mobile number: ")
    father_name = input("Enter your father's name: ")
    aadhar = input("Enter your Aadhar card number: ")
    occupation = input("Enter your occupation: ")

    # Create a new account with the entered details
    new_account = BankAccount(name, address, mobile, father_name, aadhar, occupation)
    return new_account

# Main program
def main():
    accounts = []
    while True:
        print("\n*** Welcome to the canera bank  ***")
        print("1. Create a new account")
        print("2. View existing accounts")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            account = create_account()
            accounts.append(account)
            print("Account created successfully!")
            account.display_account_info()

        elif choice == "2":
            if accounts:
                print("\nList of Accounts:")
                for i, account in enumerate(accounts, start=1):
                    print(f"\nAccount {i}:")
                    account.display_account_info()
            else:
                print("No accounts found!")

        elif choice == "3":
            print("Exiting the system. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
1