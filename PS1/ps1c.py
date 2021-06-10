def bisection_search():
    annual_salary = float(input('Enter the starting salary: '))
    total_cost = 1000000.0
    semi_annual_raise = 0.07

    portion_down_payment = 0.25
    r = 0.04  # return rate of your investments
    down_payment = total_cost * portion_down_payment

    low = 0
    high = 10000
    steps = 0

    while low <= high:
        mid = low + (high - low) // 2
        portion_saved = mid / 10000
        total_saved, months = calculate_savings(
            portion_saved, annual_salary, semi_annual_raise, down_payment, r)

        steps += 1

        print(f'Total saved: {total_saved}, Months: {months}')

        if abs(down_payment - total_saved) <= 100 and months <= 36:
            return mid
        elif months > 36:
            low = mid + 1
            months = 0
        elif months < 36:
            high = mid - 1
            months = 0


def calculate_savings(portion_saved, annual_salary, semi_annual_raise, down_payment, r):
    monthly_salary = (annual_salary / 12) * portion_saved
    current_savings = 0.0
    months = 0

    while current_savings < down_payment:
        return_on_investment = (current_savings * r) / 12
        current_savings += (return_on_investment + monthly_salary)
        months += 1

        if months % 6 == 0:
            annual_salary += (annual_salary * semi_annual_raise)
            monthly_salary = (annual_salary / 12) * portion_saved

    return current_savings, months

    print(f'Number of months: {months}')


bisection_search()
