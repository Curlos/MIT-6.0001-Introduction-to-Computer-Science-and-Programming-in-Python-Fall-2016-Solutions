def lowestPaymentNeeded(balance, annualInterestRate):
    ''' Calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

        balance: int or float (the outstanding balance on the credit card)
        annualInterestRate: float (annual interest rate as a decimal)

        Returns the lowest fixed monthly payment as an int and a multiple of 10.
    '''
    originalBalance = balance
    monthlyInterestRate = annualInterestRate / 12.0
    minPayment = 10
    while True:

        for i in range(12):
            balance -= minPayment
            interest = monthlyInterestRate * balance
            balance += interest

        if balance <= 0:
            return minPayment
        else:
            minPayment += 10
            balance = originalBalance

    return minPayment


print('Lowest Payment: ', lowestPaymentNeeded(4773, 0.2))
