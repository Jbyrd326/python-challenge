# Dependicies
import os
import csv

#Csv Path
path_file = '/Users/jbyrd326/Desktop/Home/python-challenge/PyBank/Resources/budget_data.csv'

#Pybank Variables
months = []
pnl_changes =[]
previous_value = 0

tot_months = 0
net_pnl = 0



greatest_profit_increase_date = " "
greatest_profit_increase_amount = float("-inf")
greatest_profit_decrease_date = " "
greatest_profit_decrease_amount = float("inf")

#Read csv file & Skips first line
with open(path_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    #Prints total months
    for row in csvreader:
        if row: " "
        tot_months +=1
        net_pnl += int(row[1])

        #Getting PNL changes
        current_pnl = int(row[1])
        if tot_months> 1:
            pnl_change = current_pnl - previous_value
            pnl_changes.append(pnl_change)
            #updates the list

            #Gathering greatest Increase 
            if pnl_change > greatest_profit_increase_amount:
                greatest_profit_increase_amount = pnl_change
                greatest_profit_increase_date = row[0]

            #Gathering greatest Decrease
            if pnl_change < greatest_profit_decrease_amount:
                greatest_profit_decrease_amount = pnl_change
                greatest_profit_decrease_date = row[0]

        previous_value = current_pnl

average_pnl_change = sum(pnl_changes)/ len(pnl_changes)

#Gathering results and putting it on a Txt File
output_file = "Financial Analysis.txt"
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------\n")
    file.write(f"Total Months: {tot_months}\n")
    file.write(f"Total Profit and Loss: {net_pnl}\n")
    file.write(f"Average Change of Profif and Loss: {average_pnl_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_profit_increase_date} {greatest_profit_increase_amount}\n")
    file.write(f"Greatest Decrease in Profits: {greatest_profit_decrease_date} {greatest_profit_decrease_amount}\n")

               

#CHECK WORK (terminal)
print (f"Total Months : {tot_months}") 
print(f"Total: {net_pnl}")
print(f"Avererage Change {average_pnl_change}")
print(f"Greatest Increase in Profits: {greatest_profit_increase_date} {greatest_profit_increase_amount}")
print(f"Greatest Decrease in Profits: {greatest_profit_decrease_date} {greatest_profit_decrease_amount}")
