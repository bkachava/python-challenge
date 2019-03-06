# Script for analyzing a set of financial data called budget_data.csv. 
# The dataset is composed of two columns: Date and Profit/Losses. 

#modules to read the csv and write the txt
import os
import csv
#module to sort the list
from operator import itemgetter

def net_total(fin_list):
    # Calculate the total number of months included in the dataset
    result = 0

    for num in fin_list:
        result += int(num[1])

    return result

def chg_total(chg_list):
    # Calculate the total of the changes in "Profit/Losses" over the entire period
    result = 0

    for num in chg_list:
        result += int(num)

    return result

def average_change(fin_list):
    # Calculate the average of the changes in "Profit/Losses" over the entire period
    prof_loss = 0
    months = []
    changes = []
    ave_chg = 0.0
    first_iter = True

    for num in fin_list:
        if first_iter:
            # Store the first value to use it in the next iteration
            prof_loss = int(num[1])
            first_iter = False
        else:
            # Put the amounts in one list to calculate the changes 
            changes.append(int(num[1]) - prof_loss)
            # Put the months in another list to identify the changes
            months.append(num[0])
            # Store the amount to use it in the next iteration
            prof_loss = int(num[1])
    
    ave_chg = round(float(chg_total(changes) / len(changes)),2)

    # Join the lists to sort the results by amount and calculate the increase and the decrease
    inc_dec = zip(months,changes)
    inc_dec = list(inc_dec)
    sorted_list = sorted(inc_dec, key=itemgetter(1))

    # Obtain the greatest increase in profits (date and amount) over the entire period
    max_chg = sorted_list[-1]

    # Obtain the greatest decrease in losses (date and amount) over the entire period
    min_chg = sorted_list[0]
    
    return ave_chg, max_chg, min_chg

# The set of financial data called budget_data.csv, must be located in the folder Resources
budget_csv = os.path.abspath("Resources\\budget_data.csv")

try:
    # Code that might cause an exception
    with open(budget_csv, newline='') as csvfile:   # or newline='\n'
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        budgets = list(csvreader)

except FileNotFoundError:
    # Code to be ejecuted in case the FileNotFoundError exception arises
    print("path=" + str(os.path.abspath("Resources\\budget_data.csv")))
    print("Please check the path of the file.")

else:
    # Code to be ejecuted if the try block was successful
    net_total = net_total(budgets)

    avg_change, max_month, min_month = average_change(budgets)
    
    # Print the analysis to the terminal 
    print("Financial Analysis\n----------------------------")
    print(f'Total Months: {len(budgets)}')
    print(f'Total: $ {net_total}')
    print(f'Average Change: $ {avg_change}')
    print(f'Greatest Increase in Profits: {max_month[0]} (${max_month[1]})')
    print(f'Greatest Decrease in Profits: {min_month[0]} (${min_month[1]})')

    # Export the results to a text file
    # save the output file path
    output_file = os.path.abspath("Output\\results.txt")

    # open the output file and write the results
    with open(output_file, "w") as text_file:
        print("Financial Analysis\n----------------------------", file=text_file)
        print(f'Total Months: {len(budgets)}', file=text_file)
        print(f'Total: $ {net_total}', file=text_file)
        print(f'Average Change: $ {avg_change}', file=text_file)
        print(f'Greatest Increase in Profits: {max_month[0]} (${max_month[1]})', file=text_file)
        print(f'Greatest Decrease in Profits: {min_month[0]} (${min_month[1]})', file=text_file)
        
