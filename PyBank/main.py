# Import os and csv
import os
import csv

# Set csv path
csvpath = os.path.join("../PyBank/budget_data.csv")

# Set Variables
total_months = 0
net_money = 0
all_profits = []
max_profit = 0
date_max_profit = " "
min_profit = 0
date_min_profit = " "

# open csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # skip header
    csv_header = next(csvreader)

    # set loop for csv
    for row in csvreader:

        # create a list of profits
        all_profits.append(row[1])

        # count the numer of months 
        total_months = total_months + 1

        # determine total money 
        net_money = net_money + int(row[1])

        # find the profit of a specific month
        monthly_profit = int(row[1])

        # set loop to grab the date associated with monthly profit
        if monthly_profit > max_profit:
            max_profit = monthly_profit
            date_max_profit = row[0]    
        if monthly_profit < min_profit:
            min_profit = monthly_profit
            date_min_profit = row[0]

first_profit = all_profits[0]
last_profit = all_profits[-1]

avg_change = (int(last_profit) - int(first_profit)) // total_months
     
print("Financial Analysis")
print("---------------------")   
print(f"Total Months: {total_months}")
print(f"Total: ${net_money}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {date_max_profit} -- ${max_profit} ")
print(f"Greatest Decrease in Profits: {date_min_profit} -- ${min_profit} ")
            


        
    
    
    
