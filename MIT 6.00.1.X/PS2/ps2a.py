
def calculateDebtInAYear(balance, annualInterestRate, monthlyPaymentRate):
    ''' Calculates the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

        balance: int or float (the outstanding balance on the credit card)
        annualInterestRate: float (annual interest rate as a decimal)
        monthlyPaymentRate: float (monthlyPaymentRate)

        Returns the remaining balance after one year as a float.
    '''
    monthlyInterestRate = annualInterestRate / 12.0

    for i in range(12):
        minPayment = balance * monthlyPaymentRate
        balance -= minPayment
        interest = monthlyInterestRate * balance
        balance += interest

    return balance


balance = calculateDebtInAYear(5000.00, 0.18, 0.02)
print('Remaining balance: ', round(balance, 2))
