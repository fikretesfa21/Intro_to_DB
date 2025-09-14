Monthly_income = int(input("Enter your monthly income: "))
Monthly_expenses = int(input("Enter your monthly expenses:" ))
Monthly_savings = Monthly_income - Monthly_expenses
interest_rate = 0.05
projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * interest_rate)
print("your monthly savings are $", Monthly_savings)
print("projected savings after one year, with interest, is :$", projected_savings)
