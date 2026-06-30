from .account import Account

# RegularAccount extends Account
class RegularAccount(Account):

    def __init__(self, first_name, last_name, interest):
        # call parent constructor
        super().__init__(first_name, last_name)
        self.interest = interest
