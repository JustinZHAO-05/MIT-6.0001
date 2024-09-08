annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0.00
r = 0.04
monthly_salary = annual_salary / 12
down = total_cost * portion_down_payment

months = 0
while current_savings < down :
    current_savings += current_savings*r/12
    current_savings += annual_salary/12*portion_saved
    months += 1

print("Number of months:" , months )

