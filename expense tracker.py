#input expenses
from datetime import datetime as dt
expense_list= {}

expense = str(input("Enter Expense Type: "))
amount= int(input ("Enter Expense Amount: "))
date= dt.now().strftime("%Y-%m-%d")
f_expense= {expense: [amount,date]}
expense_list.update(f_expense)

#display input
print(expense_list)
#records processing
    #tables
    #charts
