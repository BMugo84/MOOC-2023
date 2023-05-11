class BankAccount:

    def __init__(self, account_number: str, owner: str, balance: float, annual_interest: float) :
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest

peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)
