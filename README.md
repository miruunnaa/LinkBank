A simple object-oriented banking system built in Python, demonstrating core OOP concepts such as inheritance, encapsulation, polymorphism, and method overriding.
Project Structure

linkbank/
│
├── account.py        # Base Account class
├── regular.py        # RegularAccount – extends Account with interest
├── credit.py         # CreditAccount – extends Account with debt tracking
└── test-bank.py      # Test script demonstrating all functionality
Classes

Account (account.py)

The base class for all account types.

Properties: first_name, last_name, _amount (encapsulated), currency (class variable: RON)
Methods:

deposit(amount) – adds funds to the account
withdraw(amount) – removes funds if balance allows
show_info() – returns a formatted account summary string
amount – property with getter and setter (setter currently a placeholder)



RegularAccount (regular.py)

Extends Account with an interest rate field.


Inherits all methods from Account
Adds interest attribute


CreditAccount (credit.py)

Extends Account with credit/debt functionality.


Adds _debt tracking
Overrides:

deposit(amount) – deposits funds and reduces debt
withdraw(amount) – allows balance to go negative, tracking debt
__str__() – displays balance and current debt



How to Run

Make sure your project folder is structured as a package named linkbank/, then run:

bashpython test-bank.py

Concepts Demonstrated

ConceptWhereEncapsulation_amount, __limit in AccountInheritanceRegularAccount, CreditAccount extend AccountMethod overridingwithdraw() and __str__() in CreditAccountPolymorphismdeposit() called on mixed list of account typesProperties@property getter/setter for amountClass variablescurrency = 'RON' shared across all instances

Requirements


Python 3.x
No external dependencies


Notes


This project was built as part of a Python & OOP course at Link Academy
Some features are marked TODO and are intentionally incomplete (e.g. transaction history, database integration, malicious log detection)
