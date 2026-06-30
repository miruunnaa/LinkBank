from linkbank.regular import RegularAccount
from linkbank.credit import CreditAccount
from linkbank.account import Account

vasile_account = RegularAccount("Vasile", "Popescu", 1)  # object
# print(vasile_account)

gigel_account = CreditAccount("Gigel", "Haralambie", 15)  # object
# print(gigel_account)

# TODO: Add accounts to a list

# display all account information
# print(f"{vasile_account.first_name} {vasile_account.last_name} has in account {vasile_account.amount} {Account.currency}")

# print(vasile_account.show_info())
# print(gigel_account.show_info())

print(vasile_account)  # print(vasile_account.__str__())
vasile_account.deposit(100)
print(vasile_account)
vasile_account.amount = 3
print(vasile_account.amount)
vasile_account.withdraw(15)
print(vasile_account)
vasile_account.withdraw(90)
print(vasile_account)

print(gigel_account)
gigel_account.deposit(13)
print(gigel_account)
gigel_account.withdraw(50)
print(gigel_account)
gigel_account.withdraw(10)
print(gigel_account)
gigel_account.deposit(20)
print(gigel_account)

accounts = [vasile_account, gigel_account]
for account in accounts:
    account.deposit(10)  # polymorphism

print(vasile_account, gigel_account)
vasile_account._amount = -39132132
vasile_account.withdraw(414)

# vasile_account.deposit(-313131)
