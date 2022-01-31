import time

class Wallet:
    class Transaction:
        def __init__(self, amount):
            self._amount = amount
            self.timestamp = time.time()

        def get_amount(self):
            return self._amount

    def __init__(self, initial_amount):
        self._transactions = []
        self._transactions.append(Wallet.Transaction(initial_amount))

    def add_transaction(self, tx_amount):
        self._transactions.append(Wallet.Transaction(tx_amount))

    def _sum_transactions(self):
        #sum up the transaction amounts
        total = 0
        for tx in self._transactions:
            total+= tx.get_amount()
        return total


    def get_balance(self):
        return self._sum_transactions()

    def __str__(self):
        return str(self.get_balance())

    def _repr (self):
        pass

wallets = []
wallets.append(Wallet(50))
wallets.append(Wallet(100))
wallet = Wallet(50)
wallet.add_transaction(-25)
print(wallet.get_balance())