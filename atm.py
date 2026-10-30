#ATM cash withdrawal simulator

Transaction_fee = 30.0


try:
    balance = float(input("Enter your current account balance: "))
    withdrawal = float(input("Enter the amount to withdraw: "))

    if withdrawal <= 0:
        print("Error: Withdrawal amount must be greater than zero.")
        