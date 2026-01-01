'''creating a Bank program that managed a particular person's account '''

class Account():
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, m):
        self._balance -= m

def main():
    account = Account()
    print("Initial account situation...")
    print(f"Balance: {account.balance}")
    account.deposit(100)
    print("After deposit...")
    print(f"Balance: {account.balance}")
    account.withdraw(50)
    print("After withdrawal...")
    print(f"Balance: {account.balance}")

if __name__=="__main__":
    main()
