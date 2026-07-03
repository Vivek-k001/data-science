class Bank:
    def __init__(self):
        self.acc_no = 0
        self.bal = 0
        print(self.bal)

    def addBank(self):
        self.acc_no = int(input("Enter the bank account number: "))

    def deposit(self):
        amt = int(input("Enter the amount to deposit: "))
        self.bal += amt
        print("\nAmount deposited!")

    def withdraw(self):
        amt = int(input("Enter the amount to withdraw: "))
        if amt <= self.bal:
            self.bal -= amt
            print("Amount withdrawn!")
        else:
            print("Insufficient balance!")

    def transfer(self):
        print("Transfer")

    def balance(self):
        print("Total balance:", self.bal)


b = Bank()
ch = -1

while ch != 0:
    print("\n1 - Add bank account")
    print("2 - Deposit amount")
    print("3 - Withdraw amount")
    print("4 - Transfer")
    print("5 - Show balance")
    print("0 - Exit")

    ch = int(input("Enter the choice: "))

    if ch == 1:
        b.addBank()
    elif ch == 2:
        b.deposit()
    elif ch == 3:
        b.withdraw()
    elif ch == 4:
        b.transfer()
    elif ch == 5:
        b.balance()
