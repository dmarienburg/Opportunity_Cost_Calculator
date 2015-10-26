class CalculateDataTuple:
    """
    This class will take month, debt, income, interest_rate, liabilities.
    It will return a (month, debt) tuple.
    """
    def __init__(self, debt=0, income=0, interest_rate=0, liabilities=0, month=0):
        self.debt = debt
        self.income = income
        self.interest_rate = interest_rate
        self.liabilities = liabilities
        self.month = month
        self.calculate_debt()

    def calculate_debt(self):
        new_debt = self.debt + (self.debt * self.interest_rate) - self.income + self.liabilities
        return self.month, new_debt
