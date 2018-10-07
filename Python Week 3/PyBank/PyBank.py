import os
import csv
import math

budget_data = os.path.join("..","Resources","budget_data.csv")
result_data = os.path.join("..","Results", "Results_PyBank.txt")

total_months = 0
total_net_amount = 0
profit_loss_change = 0
stored_change = []
stored_month_max = []
stored_month_min = []
average_profit_loss = 0
length_changes = 0
sum_profit_loss_change = 0
max_change = 0
min_change = 0

with open(budget_data, "r") as budget_data_csv:
    csv_reader = csv.reader(budget_data_csv, delimiter=",")
    header_csv = next(csv_reader)
    for row in csv_reader:

        #calculate total months by adding 1 as it looks through the sheet
        total_months+=1

        #cast column 2 to a float and then add the values as it looks through the sheet
        stored_profit_loss = float(row[1])
        total_net_amount += stored_profit_loss

        if total_months > 1:
            profit_loss_change = stored_profit_loss - old_profit_loss
        old_profit_loss = stored_profit_loss
        stored_month_max.append(row[0])
        stored_month_min.append(row[0])
        stored_change.append(profit_loss_change)
    max_change = max(stored_change)
    index_change_max = stored_change.index(max_change)
    index_change_min = stored_change.index(min_change)
    min_change = min(stored_change)
    #prints total months
    print("There are " + str(total_months) + " recorded in this dataset.")
    #prints sum of total amount in 2 column
    print("The total net income is $" + str(total_net_amount) + ".")
    #print(stored_change)
    length_changes = len(stored_change) - 1
    #print(length_changes)
    sum_profit_loss_change = sum(stored_change)
    #average of changes
    print(f"The Average change in profit is ${sum_profit_loss_change/length_changes:.2f}.")
    #prints highest change in profit loss column
    print("The Highest change was $" + str(max_change) +".")
    #prints the lowest value of change in profit loss column
    print("The Lowest change was $" + str(min_change) + ".")

    result = (f"""Analysis of Data
    ================================================
    There are {total_months} recorded in this datasheet.
    The total net income is ${total_net_amount}
    The average change in profit is ${sum_profit_loss_change/length_changes:.2f}
    The highest change in the profit/loss column was {stored_month_max[index_change_max]} "$" {max_change}
    THe higheest decrease in the profit/loss colum was {stored_month_min[index_change_min]} "$" {min_change}""")

    with open(result_data, 'w') as r:
        r.write(result)





