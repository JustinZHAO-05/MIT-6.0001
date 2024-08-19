annual_salary_0 = float(input("Enter the starting salary: "))
portion_saved_low = 0
portion_saved_high = 10000
total_cost = 1000000
semi_annual_raise = 0.04
portion_down_payment = 0.25
current_savings = 0.00
r = 0.04
down = total_cost * portion_down_payment
months = 36
portion_saved_int = (portion_saved_high + portion_saved_low) / 2
steps = 0

annual_salary_1 = annual_salary_0
for i in range (1,months+1) :
        current_savings += current_savings*r/12
        current_savings += annual_salary_1/12
        if i%6 == 0 and i != 0:
            annual_salary_1 += annual_salary_1*semi_annual_raise

if current_savings < down:
     print("It is not possible to pay the down payment in three years.")
else:

    while abs(current_savings - down) >= 100:
        current_savings = 0.00 
        annual_salary_1 = annual_salary_0
        steps += 1
        for i in range (1,months+1) :
            current_savings += current_savings*r/12
            current_savings += annual_salary_1/12*(portion_saved_int/10000)
            if i%6 == 0 and i != 0:
                annual_salary_1 += annual_salary_1*semi_annual_raise
    
        if current_savings < down:
            portion_saved_low = portion_saved_int
        else :
            portion_saved_high = portion_saved_int

        portion_saved_int = (portion_saved_high + portion_saved_low) / 2 
    
    


    print("Best savings rate:" , round(portion_saved_int/10000 , 4))
    print("Steps in bisection search:" , steps)