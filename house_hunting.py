# variables I can give a value to
portion_down_payment = 0.25
r = 0.04
current_savings = 0
month = 0

# variables the user will give a value to
total_cost = float(input('What is the cost of your home? '))
annual_salary = float(input('What is your anual salary? '))
portion_saved = float(input('How much money will you save each month? Please enter the amount in decimal form as a percentage of your monthly salary (ex: 0.1 for 10%) '))

# variables to convert yearly values to monthly values
monthy_r = r/12
monthly_salary = annual_salary/12

# what will the downpayment equal
down_payment = total_cost * portion_down_payment


# while loop syntax
# while n > 0:
# ...     n -= 1
# ...     print(n)
while current_savings <= down_payment:


