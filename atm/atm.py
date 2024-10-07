class ATM:
    def __init__(self) :
        self.balance = 0;
        
    def check_balance(self):
        return self.balance
        
    def deposite(self, amount):
        if amount <= 0:
            raise ValueError('deposite amount must be positive.')
    
        self.balance += amount
        return True
            
    def withdraw(self , amount):
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive.')
        if amount > self.balance:
            raise ValueError('Insufficient funds.')

        self.balance -= amount
            
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
            balance = atm.check_balance()
            print(f"Your current balance is: ${balance}")
        elif choice == '2':
            while True:
                try:
                    amount = float(input('Enter the amount to deposit: '))
                    atm.deposite(amount)
                    print(f"Successfully deposited ${amount}")  
                    break
                except ValueError as e:
                    print(e)
        elif choice == '3':
             while True:
                try:
                    float(input('Enter the amount to withdraw: '))   
                    atm.withdraw(amount);
                    print(f"Successfully withdrow ${amount}")
                    break
                except ValueError as e:
                    print(e)
        elif choice == '4':
            print('Thank you for using the ATM')
            break
        else:
            print('Invalid choicce please try again')
    
if __name__ == "__main__":
    main()
            