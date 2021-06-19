def lowestPaymentNeededBisectionSearch(balance, annualInterestRate):
    ''' Calculates the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

        balance: int or float (the outstanding balance on the credit card)
        annualInterestRate: float (annual interest rate as a decimal)
        monthlyPaymentRate: float (monthlyPaymentRate)

        Returns the remaining balance after one year as a float.
    '''
    originalBalance = balance
    monthlyInterestRate = annualInterestRate / 12.0
    low = balance / 12
    high = (balance * ((1 + monthlyInterestRate)**12)) / 12.0

    while low < high:
        mid = low + (high - low) // 2

        for i in range(12):
            balance -= mid
            interest = monthlyInterestRate * balance
            balance += interest

        if abs(round(balance + 0, 2)) <= 0.07:
            return round(mid, 2)
        elif balance > 0:
            low = mid + .01
        elif balance < 0:
            high = mid + .01

        balance = originalBalance


print('Lowest Payment: ', lowestPaymentNeededBisectionSearch(320000, 0.2))
