from .account import Account

class CreditAccount(Account):

    def __init__(self, first_name, last_name, interest):
        super().__init__(first_name, last_name)
        self.interest = interest
        self._debt = 0

    def deposit(self, amount):
        super().deposit(amount)
        self._debt -= amount

    # overriding parent method
    def withdraw(self, amount):
        self._amount = self._amount - amount

        if self._amount < 0:
            self._debt = abs(self._amount)

    def __str__(self):  # TODO: Remove F_ and L_
        return super().__str__() + f' and debt of {self._debt} {Account.currency}'
