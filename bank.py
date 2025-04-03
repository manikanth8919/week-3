balance=10000
def credit(balance,amount):
    balance=amount+balance
    return balance
def debit (balance,amount):
        balance=balance-amount
        return balance
def show(balance):
            print(balance)
            
balance=1000
balance=credit(balance,200)
balance=debit(balance,300)
show(balance)
