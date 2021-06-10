annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(
    input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04  # return rate of your investments
monthly_salary = (annual_salary / 12) * portion_saved
down_payment = total_cost * portion_down_payment

months = 0

while current_savings < down_payment:
    return_on_investment = (current_savings * r) / 12
    current_savings += (return_on_investment + monthly_salary)
    months += 1

    if months % 6 == 0:
        annual_salary += (annual_salary * semi_annual_raise)
        monthly_salary = (annual_salary / 12) * portion_saved


print(f'Number of months: {months}')
