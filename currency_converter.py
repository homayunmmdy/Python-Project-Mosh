while True:
    try:
        amount = float(input('Enter the amount: '))
        if amount <= 0:
            raise ValueError()
        break
    except ValueError:
        print('Invalid amount')
        
currencies = ('USD', 'EUR' , 'CAD')

while True:
    source_currency = input('Source currency(USD/EUR/CAD): ').upper()
    if(source_currency not in currencies):
        print('Invalid currency')
    else:
        break


while True:
    target_currency = input('Target currency(USD/EUR/CAD): ').upper()
    if(target_currency not in currencies):
        print('Invalid currency')
    else:
        break
    
exchange_rates = {
    'USD': {'EUR': 0.85 , 'CAD': 1.25},
    'EUR': {'USD': 1.18 , 'CAD': 1.74},
    'CAD': {'USD': 0.80 , 'EUR': 0.68}
}

if source_currency == target_currency:
    converted_amount = amount
else :
    converted_amount = amount  * exchange_rates[source_currency][target_currency]
print(f'{amount} {source_currency} is equal to {converted_amount:.2f}')