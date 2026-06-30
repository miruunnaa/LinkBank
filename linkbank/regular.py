from .account import Account

# class Regular Account extinde Account
class RegularAccount(Account):
    
    def __init__(self, first_name, last_name, interest):
        # apeleaza constructorul din parinte
        super().__init__(first_name, last_name)   
        self.interest = interest

    