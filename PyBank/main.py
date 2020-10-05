import os
import csv
pybank_csv = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
#making output for .txt file for analysis folder
pybank_output = os.path.join("analysis", "pybank_analysis.txt")

#clarifying our variables
total = 0
average_change = 0
greatest_increase = [" ", 0]
greatest_decrease = [" ", 0]
net_change_list =[]
total_months = 0
total_net = 0
prev_net = 0

#reading our csvfile to perform coding
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #header set
    header = next(csvreader)

    #need to establish first_row after header
    #gaining information from second column
    first_row = next(csvreader)
    total += int(first_row[1])
    total_months +=1
    #need to find values for the average of the changes
    total_net += int(first_row[1])
    prev_net += int(first_row[1])

    #can now loop through rows
    for row in csvreader:
        total_months += 1
        total += int(row[1])
        #calculating the changes and putting it into net_change_list (a list)
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]

        #greatest_increase/greatest_decrease = {" ",0}
        # using > and < to find most and the least
        if net_change > greatest_increase[1]:
            greatest_increase[0] =row[0]
            greatest_increase[1] =net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] =row[0]
            greatest_decrease[1] =net_change

#to 2 decimal places and equation for average_change outside of loop
average_change = str(round((sum(net_change_list) / (total_months - 1)), 2))

#what will be printed and the output in the .txt fileS
output = (
    f"\nFinancial Analysis\n"
    f"-----------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {str(greatest_increase[0])}, (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {str(greatest_decrease[0])}, (${greatest_decrease[1]})\n")

print(output)

with open(pybank_output, "a") as txt_file:
    txt_file.write(output)