#!/usr/bin/env python
# coding: utf-8

# In[64]:


import os
import csv

csvpath_load = os.path.join('.','budget_data.csv')
file_to_output = os.path.join("financial_analysis.txt")

#print(csvpath_load)

with open(csvpath_load, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    prev_profit = 0
    net_change = 0
    
    greatest_increase = 0
    greatest_decrease = 0
    
    # First row with data i.e. Jan-10
    first_row = next(csvreader)
    
    # Set num_months to 1, because we start loop from row 2
    num_months = 1
    total_profit = int(first_row[1])
    prev_profit = int(first_row[1])
 

    # Read each row starting from row 2
    for row in csvreader:
#         print(row[0],',', row[1])
        month = row[0]
        current_profit = int(row[1])
        
        num_months = num_months + 1
        total_profit = total_profit + current_profit
        
        change_in_profit = current_profit - prev_profit
        net_change = net_change + change_in_profit
        prev_profit = current_profit
        
        if change_in_profit >= greatest_increase:
            greatest_increase = change_in_profit
            greatest_increase_month = row[0]
        if change_in_profit <= greatest_decrease:
            greatest_decrease = change_in_profit
            greatest_decrease_month = row[0]
            
            
       
    # Calculate avg current_profit after net_current_profit and num_months are finalized, 1 less change then number of months
    avg_change_profit = net_change/(num_months - 1)
    
#     print(num_months)
#     print(total_profit)
#     print(avg_change_profit)
#     print(greatest_increase, greatest_increase_month)
#     print(greatest_decrease, greatest_decrease_month)
    
    output = (
    f"\nFinancial Analysis\n"
    f"--------------------\n"
    f"Total Months: {num_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${avg_change_profit:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
    )
    
    print(output)
    
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)


# In[ ]:




