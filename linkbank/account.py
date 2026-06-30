class Account(object):

    currency = 'RON'  # class property

    def __init__(self, first_name, last_name):
        self.first_name = 'F_' + first_name
        self.last_name = 'L_' + last_name
        self._amount = 0  # encapsulation
        self.__limit = 100 * 1000

    @property
    def amount(self):  # getter
        # SELECT amount FROM accounts...
        # self._amount = from_database
        return self._amount

    @amount.setter
    def amount(self, amount):
        # TODO: Add malicious log
        pass  # self._amount = amount

    def __str__(self):  # TODO: Remove F_ and L_
        return f"{self.first_name} {self.last_name} has in account {self._amount} {Account.currency}"

    def show_info(self):
        return f"{self.first_name} {self.last_name} has in account {self._amount} {Account.currency}"

    def deposit(self, amount):
        if amount < 0:
            return

        # TODO: Add transaction history
        self._amount += amount

    def withdraw(self, amount):

        if self._amount - amount < 0:
            return

        # INSERT INTO transactions ...
        self._amount -= amount
