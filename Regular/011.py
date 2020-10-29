'''
Let's enrich an Account class by adding dunder (aka special) methods to support the following:

X length of the object: len(acc) returns the number of transactions
account comparison: acc1 >,<,>=.<=,== acc2 returns a boolean comparing account balances
X indexing: acc[n] shows the nth transaction onaccount (0 based)
X iteration: list(acc) returns a sequence of account transactions
X operator overloading: acc + int and acc - int can be used to add/subtract money
X string representation: str(acc) returns NAME account - balance: INT
The provided template already does some setup for you.
'''


class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)
    

    # add dunder methods below

    def __getitem__(self, n):
        return self._transactions[n]

    def __len__(self):
        return len(self._transactions)

    def __eq__(self,other):
        return self.balance == other.balance

    def __lt__(self,other):
        return self.balance < other.balance
    
    def __ge__(self,other):
        return self.balance >= other.balance

    def __le__(self,other):
        return self.balance <= other.balance

    def __add__(self, transaction):
        if type(transaction) != int:
            raise ValueError
        self._transactions.append(transaction)

    def __sub__(self, transaction):
        if type(transaction) != int:
            raise ValueError
        self._transactions.append(-transaction)

    def __str__(self):
        return(f'{self.name} account - balance: {self.balance}')


if __name__ == "__main__":
    a = Account('acc', 5)
    a + 5
    a - 3
    print(list(a))
    print(len(a))
    print(str(a))