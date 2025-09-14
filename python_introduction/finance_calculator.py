income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: ))
saving = income - expenses
print("your monthly savings are $", saving)
print("projected savings after one year, with interest, is :$", saving * 12 + (saving * 12 *0.05))
