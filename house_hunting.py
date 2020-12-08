# variables I can give a value to
portion_down_payment = 0.25
r = 0.04
current_savings = 0
months = 0


# variables the user will give a value to
total_cost = float(input('What is the cost of your home? '))
annual_salary = float(input('What is your anual salary? '))
portion_saved = float(input('How much money will you save each month? Please enter the amount in decimal form as a percentage of your monthly salary (ex: 0.1 for 10%) '))
print(type(portion_down_payment))

# variables to convert yearly values to monthly values
monthly_r = r/12
monthly_salary = annual_salary/12

# what will the downpayment equal
down_payment = int(total_cost * portion_down_payment)


# while loop syntax
# while n > 0:
# ...     n -= 1
# ...     print(n)
while current_savings < down_payment:

    # At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary ​(monthly_r).
    # In Python, While Loops is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed. 
    # formula to increase current savings:
    current_savings += (portion_saved * monthly_salary) + (current_savings * monthly_r)
    # increase by one month until loop condition is met:
    months += 1
    years_to_save = months/12

# We are printing the amount of time it takes to save enough money for a down payment
print(f'it will take {years_to_save} years to save your down payment of {down_payment}$.')


