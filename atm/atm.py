class ATM:
    def __init__(self) :
        self.balance = 0;
        
    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
        
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}")
        else:
            print('Deposit amount must be positive')    
            
    def withdraw(self , amount):
        if amount > self.balance:
            print('Insufficient funds.')
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            self.balance -= amount
            print(f"Successfully withdrow ${amount}")
            
def main():
    atm = ATM();
    while True:
        print('\nWelcom to the ATM!')
        print('1. Check balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        
        choice = input('Please choose an option: ')
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            while True:
                try:
                    amount = float(input('Enter the amount to deposit: '))
                    atm.deposite(amount)
                    break
                except ValueError:
                    print('Please enter a valid number: ')
        elif choice == '3':
             while True:
                try:
                    float(input('Enter the amount to withdraw: '))
                    atm.withdraw(amount)
                    break
                except ValueError:
                    print('Please enter a valid number')
        elif choice == '4':
            print('Thank you for using the ATM')
            break
        else:
            print('Invalid choicce please try again')
    
if __name__ == "__main__":
    main()
            