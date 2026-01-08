accounts = {
    1001: {"name": "Ali", "pin": 1234, "balance": 5000.0},
    1002: {"name": "Ahmed", "pin": 4321, "balance": 8000.0}
}

print("Welcome to Python ATM")

acc_no = int(input("Enter account number: "))
pin = int(input("Enter PIN: "))

if acc_no in accounts and accounts[acc_no]["pin"] == pin:
    print("Login successful!")

    while True:
        print("\n1. View Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            print(f"Current balance: Rs. {accounts[acc_no]['balance']}")

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                accounts[acc_no]["balance"] += amount
                print(f"New balance: Rs. {accounts[acc_no]['balance']}")
            else:
                print("Invalid amount")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= accounts[acc_no]["balance"] and amount > 0:
                accounts[acc_no]["balance"] -= amount
                print(
                    f"Withdrawal successful. New balance: Rs. {accounts[acc_no]['balance']}")
            else:
                print("Insufficient balance or invalid amount")

        elif choice == "4":
            print("Thank you for using Python ATM")
            break

        else:
            print("Invalid option, try again")

else:
    print("Invalid account number or PIN")
