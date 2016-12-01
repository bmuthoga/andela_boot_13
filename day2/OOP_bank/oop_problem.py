# Program that applies OOP concepts
# Bank case real world scenario
# Functions supported: Login, Check Balance, Withdraw, Deposit,
# Perform another transaction after completing one

class Customer(object):

    def __init__(self, name, args, kwargs):
        self.name = name
        self.balance = balance
        self.pin = pin

    def login(self, pin):
        attempts = 0
        while attempts < 4:
            input_pin = input('Please enter your pin: ')
            if input_pin == self.pin:
                print("Pin accepted!")
                return menu()
            else:
                print("Invalid pin. Enter pin again: ")
            attempts += 1
        print("Too many attempts. Login failed.")
        return False

    def menu(self, name):
        print("Welcome ",self.name, "! Kindly select an option:")
        print ("""1: Check balance
                  2: Deposit
                  3: Withdraw""")
        option = input("Option: ")
        if option == "1":
            return balance()
        elif option == "2":
            return deposit()
        elif option == "3":
            return withdraw()

    def balance(self, balance):
        return self.balance

    def withdraw(self):
        amount = input("Enter amount: ")
        if amount > self.balance:
            print('Insufficient funds.')
            return menu()
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        amount = input("Enter amount: ")
        self.balance += amount
        print("Amount deposited. Balance:")
        return self.balance
