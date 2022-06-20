#input expenses
from datetime import datetime as dt
expense_list= {}

while True:
    expense = input(str("Enter Expense Type: "))
    if expense != 'done':
        amount= int(input("Enter Expense Amount: "))
        date= dt.now().strftime("%Y-%m-%d")
        f_expense= {expense: [amount,date]}
        expense_list.update(f_expense)
    elif expense == 'done':
        break
    
    

#display input
print(expense_list)
#records processing
    #tables
    #charts
