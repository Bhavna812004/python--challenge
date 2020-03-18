import os
import csv

#input file + path
input_file = os.getcwd()+"\PyBank\Resources\Budget_data.csv"
output_file = os.getcwd()+"\PyBank\Summary.txt"

#revenue calculation variables
budgetdate = []
profitloss = []
profitloss_total = 0


with open(input_file, newline='') as bank_budget_data:
    reader = csv.reader(bank_budget_data, delimiter=',')
    next (reader)

    for row in reader:
        #store dates and profit/losses in array
        budgetdate.append(row[0])
        profitloss.append(row[1])


for i in profitloss:
    profitloss_total += int(i)

# Average change in profit/losses

average_change_array = []
previous_value = 0
current_value = 0
for i in profitloss:
    current_value = int(i)
    if previous_value == 0:
        previous_value = current_value
    else:
        average_change_array.append(current_value - previous_value)
        previous_value = current_value


ave_change_row_count = 0
ave_change_total = 0
for i in average_change_array:
    ave_change_row_count +=1
    ave_change_total += int(i)
average_change = format(ave_change_total/ave_change_row_count, '.2f')     

# Greatest Increase and decrease in profit/losses
greatest_value = max(average_change_array)
decreased_value = min(average_change_array)
greatest_date = budgetdate[average_change_array.index(greatest_value)+1]
decreased_date = budgetdate[average_change_array.index(decreased_value)+1]

# Header & Summary
print("Financial Analysis")
print("-----------------------------------------")
print("Total Months: " + str(len(budgetdate)))   
print("Total Profit/Losses: $" + str(profitloss_total))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + greatest_date + " ($" + str(greatest_value) + ")" )
print("Greatest Decrease in Profits: " + decreased_date + " ($" + str(decreased_value) + ")")

# Output file information
with open(output_file, 'w') as text:
    text.write("-------------------------------------------------------\n")
    text.write("  Financial Analysis\n")
    text.write("-------------------------------------------------------\n")
    text.write("  Total Months: " + str(row_number) + "\n")   
    text.write("  Total Profit/Losses: $" + str(profitloss_total) + "\n")
    text.write("  Average Change: $" + str(average_change) + "\n")
    text.write("  Greatest Increase in Profits: " + greatest_date + " ($" + str(greatest_value) + ")\n" )
    text.write("  Greatest Decrease in Profits: " + decreased_date + " ($" + str(decreased_value) + ")\n")
