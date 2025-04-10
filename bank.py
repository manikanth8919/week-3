def credit(amount,balance):
    balance = balance + amount
    return balance
    
def debit(amount,balance):
    balance = balance - amount
    return balance
    
def show_balance (balance):
    print(balance)
    
    
balance=int(input("enter the amount"))
amount=int(input("enter the amount to be credited or debited"))
sys=int(input("press 1 to credit\npress 2 to debit"))
if(sys==1):
        balance=cridit(amount,balance)
        show_balance()
if(sys==2):
        balance=debit(amount,balance)
        show_balance(balance)
