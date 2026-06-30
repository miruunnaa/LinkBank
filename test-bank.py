from linkbank.regular import RegularAccount
from linkbank.credit import CreditAccount
from linkbank.account import Account

contVasile = RegularAccount("Vasile", "Popescu", 1) # obiect
# print(contVasile)

contGigel = CreditAccount("Gigel", "Haralambie", 15) # obiect
# print(contGigel)

# TODO: Add accounts to a list

# afisam toate informatiile despre cont
# print(f"{contVasile.first_name} {contVasile.last_name} are in cont {contVasile.amount} {Account.currency}")

# print(contVasile.show_info())
# print(contGigel.show_info())

print(contVasile) # print(contVasile.__str__())
contVasile.deposit(100)
print(contVasile)
contVasile.amount = 3
print(contVasile.amount)
contVasile.withdraw(15)
print(contVasile)
contVasile.withdraw(90)
print(contVasile)

print(contGigel)
contGigel.deposit(13)
print(contGigel)
contGigel.withdraw(50)
print(contGigel)
contGigel.withdraw(10)
print(contGigel)
contGigel.deposit(20)
print(contGigel)

conturi = [contVasile, contGigel]
for cont in conturi:
    cont.deposit(10) # polimorfism

print(contVasile, contGigel)
contVasile._amount = -39132132
contVasile.withdraw(414)

# contVasile.deposit(-313131)
